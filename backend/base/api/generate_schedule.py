import datetime
import random
from .classes_for_backend import Assignment, Timeslot

MORNING_START = 8
AFTERNOON_START = 12
EVENING_START = 17


def generate_schedule(assignments: list[Assignment], days: dict, study_time_pref: int, max_study_time: int,
                      max_timeblock: int) -> list:
    hours_free = hours_available(days, max_study_time)
    schedule = days.copy()

    schedule_ags = {}
    for key in days.keys():
        schedule_ags.setdefault(key, [])

    for a in assignments:
        working_days = []
        prep_days = a.prep_days
        num_hours = a.work_per_day

        # create list of all days on which the assig should be scheduled to be worked on
        for i in range(1, prep_days):
            working_days.append(a.duedate - datetime.timedelta(days=i))
        for day in working_days:
            for hour in range(num_hours):
                slot = Timeslot(a)
                schedule_ags[day].append(slot)

    day_schedule = _resolve_schedule_conflicts(assignments, hours_free, schedule_ags, schedule)
    hourly_schedule = _schedule_hourly(days, day_schedule, study_time_pref, max_timeblock)
    json_return = convert_to_json(hourly_schedule)
    return json_return


def _resolve_schedule_conflicts(ags: list[Assignment], hours_free: dict, schedule_ags: dict, schedule: dict) -> dict:
    values = [0] * len(hours_free.keys())
    deficit_dict = {k: v for k, v in zip(hours_free.keys(), values)}

    for day in deficit_dict.keys():  # calculate hour deficit per day of semester
        deficit_dict[day] = hours_free[day] - len(schedule_ags[day])

    sorted_days_list = sorted(list(deficit_dict.keys()))  # sort days in chronological order

    free_slots = {}

    for i in range(len(sorted_days_list) - 1, -1, -1):
        # create free time slots that correspond to every under-scheduled day
        if deficit_dict[sorted_days_list[i]] > 0:
            for j in range(deficit_dict[sorted_days_list[i]]):
                # create a key for every day that has at least one free slot
                # for every free slot, make a key with a list as the value
                # (the list will hold all potential assig that can be scheduled in it)
                free_slots.setdefault(sorted_days_list[i], {}).setdefault(j, [])

        # overbooked days must be rescheduled, but the specific assig timeslots that will be
        # rescheduled are unknown right now
        if deficit_dict[sorted_days_list[i]] < 0:
            d = sorted_days_list[i]
            for j in range(len(schedule_ags[d])):
                free_slots.setdefault(d, {}).setdefault(j, [])

    for i in range(len(sorted_days_list) - 1, -1, -1):
        day = sorted_days_list[i]

        # check if the day is overbooked and slots in it must be rescheduled to a diff day
        if deficit_dict[day] < 0:
            # iterate through assignment booked on that day to decide which one(s) should be rescheduled
            for agn in schedule_ags[day]:
                start_day_index = sorted_days_list.index(agn.start_datetime)
                end_day_index = sorted_days_list.index(agn.duedate)

                for reschedule_day_index in range(start_day_index, end_day_index + 1):
                    # check if there are any free slots available within the due date of the assig
                    # so that the assignment can be rescheduled
                    reschedule_day = sorted_days_list[reschedule_day_index]

                    if reschedule_day in free_slots:
                        # iterate through every free slot available on that day
                        for free_slot in free_slots[reschedule_day]:
                            free_slots[reschedule_day][free_slot].append(agn)

            # once all the assignments have been assigned to potential reschedule dates, clear all scheduled
            # timeslots for this day
            schedule_ags[day] = []

    final_schedule = _find_optimal_schedule(schedule_ags, free_slots)
    return final_schedule


def _find_optimal_schedule(schedule_ags: dict, free_slots: dict) -> dict:
    already_scheduled_ags = []

    for day in free_slots.keys():
        for slot in free_slots[day]:
            highest_priority = None
            for a in free_slots[day][slot]:
                if a.ROI > highest_priority.ROI and a not in already_scheduled_ags:
                    highest_priority = a
            if highest_priority is not None:
                schedule_ags[day].append(highest_priority)
                already_scheduled_ags.append(highest_priority)

    return schedule_ags


def _schedule_hourly(days: dict, day_schedule: dict, study_time_pref: int, max_timeblock: int) -> dict:
    for day in days.keys():
        if study_time_pref == 0:  # study pref is morning
            hour = MORNING_START
            prev_scheduled = None
            prev_scheduled_count = 0

            a_to_schedule = {}

            for slot in day_schedule[day]:
                a_to_schedule.setdefault(slot.ag, []).append(slot)

            while hour < 22 and len(a_to_schedule) > 0:  # change to user's day start and end time
                if days[day][hour] is None:
                    if prev_scheduled is not None and prev_scheduled in a_to_schedule and prev_scheduled_count < max_timeblock:
                        pass

                    elif prev_scheduled is None or prev_scheduled not in a_to_schedule:
                        a = random.choice(list(a_to_schedule.keys()))
                        prev_scheduled = a

                    elif prev_scheduled_count >= max_timeblock:
                        a = prev_scheduled
                        while a != prev_scheduled:  # choose another ag that was not previously scheduled
                            a = random.choice(list(a_to_schedule.keys()))
                        prev_scheduled = a

                    slot = a_to_schedule[prev_scheduled].pop()
                    days[day][hour] = slot
                    prev_scheduled_count += 1

                    if len(a_to_schedule[slot.ag]) == 0:
                        a_to_schedule.pop(slot.ag)

                else:  # reset variables
                    prev_scheduled = None
                    prev_scheduled_count = 0

                hour += 1

        elif study_time_pref == 1:  # study pref is afternoon
            hour = AFTERNOON_START
            prev_scheduled = None
            prev_scheduled_count = 0
            first_scheduled = None
            first_scheduled_count = 0

            a_to_schedule = {}

            for slot in day_schedule[day]:
                a_to_schedule.setdefault(slot.ag, []).append(slot)

            while hour < 22 and len(a_to_schedule) > 0:  # change to user's day start and end time

                if days[day][hour] is None:
                    if prev_scheduled is not None and prev_scheduled in a_to_schedule and prev_scheduled_count < max_timeblock:
                        first_scheduled_count += 1

                    elif prev_scheduled is None or prev_scheduled not in a_to_schedule:
                        a = random.choice(list(a_to_schedule.keys()))
                        prev_scheduled = a
                        if first_scheduled is None:
                            first_scheduled = a
                            first_scheduled_count += 1

                    elif prev_scheduled_count >= max_timeblock:
                        a = prev_scheduled
                        while a != prev_scheduled:  # choose another ag that was not previously scheduled
                            a = random.choice(list(a_to_schedule.keys()))
                        prev_scheduled = a

                    slot = a_to_schedule[prev_scheduled].pop()
                    days[day][hour] = slot
                    prev_scheduled_count += 1

                    if len(a_to_schedule[slot.ag]) == 0:
                        a_to_schedule.pop(slot.ag)

                else:  # reset variables
                    prev_scheduled = None
                    prev_scheduled_count = 0

                hour += 1

            if len(day_schedule[day]) > 0:
                hour = AFTERNOON_START - 1
                prev_scheduled = first_scheduled
                prev_scheduled_count = first_scheduled_count

                while hour >= 8 and len(a_to_schedule) > 0:  # change to user's day start and end time

                    if days[day][hour] is None:
                        if prev_scheduled is not None and prev_scheduled in a_to_schedule and prev_scheduled_count < max_timeblock:
                            pass

                        elif prev_scheduled is None or prev_scheduled not in a_to_schedule:
                            a = random.choice(list(a_to_schedule.keys()))
                            prev_scheduled = a

                        elif prev_scheduled_count >= max_timeblock:
                            a = prev_scheduled
                            while a != prev_scheduled:  # choose another ag that was not previously scheduled
                                a = random.choice(list(a_to_schedule.keys()))
                            prev_scheduled = a

                        slot = a_to_schedule[prev_scheduled].pop()
                        days[day][hour] = slot
                        prev_scheduled_count += 1

                        if len(a_to_schedule[slot.ag]) == 0:
                            a_to_schedule.pop(slot.ag)

                    else:  # reset variables
                        prev_scheduled = None
                        prev_scheduled_count = 0

                    hour -= 1

        elif study_time_pref == 2:  # study pref is evening
            hour = EVENING_START
            prev_scheduled = None
            prev_scheduled_count = 0
            first_scheduled = None
            first_scheduled_count = 0

            a_to_schedule = {}

            for slot in day_schedule[day]:
                a_to_schedule.setdefault(slot.ag, []).append(slot)

            while hour < 22 and len(a_to_schedule) > 0:  # change to user's day start and end time

                if days[day][hour] is None:
                    if prev_scheduled is not None and prev_scheduled in a_to_schedule and prev_scheduled_count < max_timeblock:
                        first_scheduled_count += 1

                    elif prev_scheduled is None or prev_scheduled not in a_to_schedule:
                        a = random.choice(list(a_to_schedule.keys()))
                        prev_scheduled = a
                        if first_scheduled is None:
                            first_scheduled = a
                            first_scheduled_count += 1

                    elif prev_scheduled_count >= max_timeblock:
                        a = prev_scheduled
                        while a != prev_scheduled:  # choose another ag that was not previously scheduled
                            a = random.choice(list(a_to_schedule.keys()))
                        prev_scheduled = a

                    slot = a_to_schedule[prev_scheduled].pop()
                    days[day][hour] = slot
                    prev_scheduled_count += 1

                    if len(a_to_schedule[slot.ag]) == 0:
                        a_to_schedule.pop(slot.ag)

                else:  # reset variables
                    prev_scheduled = None
                    prev_scheduled_count = 0

                hour += 1

            if len(day_schedule[day]) > 0:
                hour = EVENING_START - 1
                prev_scheduled = first_scheduled
                prev_scheduled_count = first_scheduled_count

                while hour >= 8 and len(a_to_schedule) > 0:  # change to user's day start and end time

                    if days[day][hour] is None:
                        if prev_scheduled is not None and prev_scheduled in a_to_schedule and prev_scheduled_count < max_timeblock:
                            pass

                        elif prev_scheduled is None or prev_scheduled not in a_to_schedule:
                            a = random.choice(list(a_to_schedule.keys()))
                            prev_scheduled = a

                        elif prev_scheduled_count >= max_timeblock:
                            a = prev_scheduled
                            while a != prev_scheduled:  # choose another ag that was not previously scheduled
                                a = random.choice(list(a_to_schedule.keys()))
                            prev_scheduled = a

                        slot = a_to_schedule[prev_scheduled].pop()
                        days[day][hour] = slot
                        prev_scheduled_count += 1

                        if len(a_to_schedule[slot.ag]) == 0:
                            a_to_schedule.pop(slot.ag)

                    else:  # reset variables
                        prev_scheduled = None
                        prev_scheduled_count = 0

                    hour -= 1

    return days


def hours_available(days: dict, maximum_study_time: int) -> dict:
    values = [0] * len(days.keys())
    new_schedule = {k: v for k, v in zip(days.keys(), values)}

    for day in days.keys():
        for hour in range(8, 21):  # change to user start and end time
            day_event = days[day][hour]
            if day_event is None:
                new_schedule[day] += 1

    for day in new_schedule:
        new_schedule[day] = min(new_schedule[day], maximum_study_time)

    return new_schedule


def convert_to_json(input_calendar: dict) -> list:
    final_list = []
    for date in input_calendar:
        for hour in range(0, 24):
            if input_calendar[date][hour] is not None and isinstance(input_calendar[date][hour], Timeslot):
                final_list.append({
                    "title": input_calendar[date][hour].name,
                    "date": str(date),
                    "display": "block",
                    "start": str(date) + "T" + str(hour) + ":00:00",
                    "end": str(date) + "T" + str(hour + 1) + ":00:00"
                })
            elif input_calendar[date][hour] is not None and not isinstance(input_calendar[date][hour], Timeslot):
                final_list.append({
                    "title": input_calendar[date][hour],
                    "date": str(date),
                    "display": "block",
                    "start": str(date) + "T" + str(hour) + ":00:00",
                    "end": str(date) + "T" + str(hour + 1) + ":00:00"
                })
    return final_list
