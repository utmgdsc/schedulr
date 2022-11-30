import calendar
import csv
import datetime
import math
import random


MORNING_START = 8
AFTERNOON_START = 12
EVENING_START = 17


class Assignment:
    def __init__(self, name: str, prep: int, weight: int, due: datetime.date):
        self.name = name
        self.preptime = prep
        self.prep_days = prep + 4
        self.start_datetime = due - datetime.timedelta(days=self.prep_days)
        self.duedate = due
        self.work_per_day = math.ceil(prep/self.prep_days)
        self.ROI = weight / self.preptime


class Timeslot:
    def __init__(self, ag: Assignment):
        self.ag = ag
        self.ROI = ag.ROI
        self.name = ag.name
        self.start_datetime = ag.start_datetime
        self.duedate = ag.duedate
        self.prep_days = ag.prep_days


def generate_schedule(assignments: list[Assignment], days: dict, study_time_pref: int, max_study_time: int, max_timeblock: int) -> list:
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

    for i in range(len(sorted_days_list)-1, -1, -1):
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
                    # so that the assig can be rescheduled
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
                a_to_schedule.setdefault(slot.a, []).append(slot)

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
                a_to_schedule.setdefault(slot.a, []).append(slot)

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


def user_input(File_name: str) -> tuple:
    with open(File_name, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    study_time_preference = data[0]
    if data[0] == "morning":
        study_time_preference = 0
    elif data[0] == "noon":
        study_time_preference = 1
    elif data[0] == "evening":
        study_time_preference = 2
    maximum_study_time = data[1]
    study_days_not_available = data[2]
    return study_time_preference, maximum_study_time, study_days_not_available


def winter_list_generator() -> dict:
    # winter_list = {}
    # year = 2023
    # for month1 in range(1, 5):
    #     final_dict = {}
    #     num_days = calendar.monthrange(year, month1)[1]
    #     days = [datetime.date(year, month1, day) for day in range(1, num_days + 1)]
    #     for day in days:
    #         final_dict[day] = [None] * 24
    #     winter_list[month1] = final_dict
    # return winter_list
    winter_list = {}
    year = 2023
    for month1 in range(1, 5):
        # final_dict = {}
        num_days = calendar.monthrange(year, month1)[1]
        days = [datetime.date(year, month1, day) for day in range(1, num_days + 1)]
        for day in days:
            winter_list[day] = [None] * 24
        # winter_list[month1] = final_dict
    return winter_list


def get_dates_for_weekday_name(weekday_name: str) -> list:
    year = 2023
    month = 1
    day = 1
    date = datetime.date(year, month, day)
    dates = []
    while date.year == year and date.month <= 4:
        if date.strftime("%A") == weekday_name:
            dates.append(date)
        date += datetime.timedelta(days=1)
    return dates


def read_mock_data(file_name: str) -> list:
    with open(file_name, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def get_event_name(event: list) -> str:
    return event[0]


def get_event_start_time(event: list) -> int:
    a = event[1].strip()
    return int(a[0:2])


def get_event_end_time(event: list) -> int:
    return get_event_start_time(event) + int(event[2].strip())


def get_event_days(event: list) -> str:
    return event[3].strip()


def populate_winter_calendar_with_lecture_events(File_name: str) -> dict:
    # winter_list = winter_list_generator()
    # data = read_mock_data(File_name)
    # for event in data:
    #     event_name = get_event_name(event)
    #     event_start_time = get_event_start_time(event)
    #     event_end_time = get_event_end_time(event)
    #     event_days = get_event_days(event)
    #     dates = get_dates_for_weekday_name(event_days)
    #     for date in dates:
    #         for i in range(event_start_time, event_end_time + 1):
    #             winter_list[date.month][date][i] = event_name
    # return winter_list
    winter_list = winter_list_generator()
    data = read_mock_data(File_name)
    for event in data:
        event_name = get_event_name(event)
        event_start_time = get_event_start_time(event)
        event_end_time = get_event_end_time(event)
        event_days = get_event_days(event)
        dates = get_dates_for_weekday_name(event_days)
        for date in dates:
            for i in range(event_start_time, event_end_time):
                winter_list[date][i] = event_name
    return winter_list


def convert_to_json(input_calendar: dict) -> list:
    final_list = []
    for date in input_calendar:
        for hour in range(0, 24):
            if input_calendar[date][hour] is not None:
                final_list.append({
                    "title": input_calendar[date][hour].name,
                    "date": str(date),
                    "display": "block",
                    "start": str(date) + "T" + str(hour) + ":00:00",
                    "end": str(date) + "T" + str(hour + 1) + ":00:00"
                })
    return final_list


def convert_winter_calender_to_dict_list(winter_calender: dict) -> list:
    final_list = []
    # for month in winter_calender:
    #     for date in winter_calender[month]:
    #         for hour in range(0, 24):
    #             if winter_calender[month][date][hour] is not None:
    #                 final_list.append({
    #                     "title": winter_calender[month][date][hour],
    #                     "date": str(date),
    #                     "display": "block",
    #                     "start": str(date) + "T" + str(hour) + ":00:00",
    #                     "end": str(date) + "T" + str(hour + 1) + ":00:00"
    #                 })
    # return final_list
    for date in winter_calender:
        for hour in range(0, 24):
            if winter_calender[date][hour] is not None:
                final_list.append({
                    "title": winter_calender[date][hour],
                    "date": str(date),
                    "display": "block",
                    "start": str(date) + "T" + str(hour) + ":00:00",
                    "end": str(date) + "T" + str(hour + 1) + ":00:00"
                })
    return final_list


def remove_days_from_winter_calendar(winter_calendar: dict, days_to_remove: list) -> tuple:
    temp_removed_days = {}
    for day in days_to_remove:
        dates_to_remove = get_dates_for_weekday_name(day)
        for date in dates_to_remove:
            temp_removed_days[date] = winter_calendar[date]
            del winter_calendar[date]
    return winter_calendar, temp_removed_days


def merge_winter_calendar_with_removed_days(winter_calendar: dict, removed_days: dict) -> dict:
    for date in removed_days:
        winter_calendar[date] = removed_days[date]
    return winter_calendar


def generate_events(File_name: str) -> list:
    # study_preference, maximum_study_time, study_days_not_available = user_input('data.csv')
    # year_list = winter_list_generator()
    a = populate_winter_calendar_with_lecture_events(File_name)
    b = convert_winter_calender_to_dict_list(a)
    return b


a1 = Assignment("A1", 12, 15, datetime.date(year=2022, month=10, day=30))
a2 = Assignment("A2", 25, 30, datetime.date(year=2022, month=10, day=27))
a3 = Assignment("A3", 10, 18, datetime.date(year=2022, month=10, day=10))

days = {datetime.date(year=2022, month=9, day=30): [None]*24,datetime.date(year=2022, month=9, day=28): [None]*24, datetime.date(year=2022, month=9, day=26): [None]*24,datetime.date(year=2022, month=9, day=27): [None]*24,datetime.date(year=2022, month=9, day=29): [None]*24, datetime.date(year=2022, month=10, day=1): [None]*24, datetime.date(year=2022, month=10, day=2): [None]*24, datetime.date(year=2022, month=10, day=3): [None]*24, datetime.date(year=2022, month=10, day=4): [None]*24, datetime.date(year=2022, month=10, day=5): [None]*24, datetime.date(year=2022, month=10, day=6): [None]*24, datetime.date(year=2022, month=10, day=7): [None]*24, datetime.date(year=2022, month=10, day=8): [None]*24, datetime.date(year=2022, month=10, day=9): [None]*24, datetime.date(year=2022, month=10, day=10): [None]*24, datetime.date(year=2022, month=10, day=11): [None]*24, datetime.date(year=2022, month=10, day=12): [None]*24, datetime.date(year=2022, month=10, day=13): [None]*24,datetime.date(year=2022, month=10, day=14): [None]*24,datetime.date(year=2022, month=10, day=15): [None]*24,datetime.date(year=2022, month=10, day=16): [None]*24,datetime.date(year=2022, month=10, day=17): [None]*24,datetime.date(year=2022, month=10, day=18): [None]*24,datetime.date(year=2022, month=10, day=19): [None]*24,datetime.date(year=2022, month=10, day=20): [None]*24,datetime.date(year=2022, month=10, day=21): [None]*24,datetime.date(year=2022, month=10, day=22): [None]*24,datetime.date(year=2022, month=10, day=23): [None]*24,datetime.date(year=2022, month=10, day=24): [None]*24,datetime.date(year=2022, month=10, day=25): [None]*24,datetime.date(year=2022, month=10, day=26): [None]*24,datetime.date(year=2022, month=10, day=27): [None]*24,datetime.date(year=2022, month=10, day=28): [None]*24,datetime.date(year=2022, month=10, day=29): [None]*24,datetime.date(year=2022, month=10, day=30): [None]*24}
study_time_pref = 0
max_study_time = 10
max_timeblock = 3

print(generate_schedule([a1, a2, a3], days, study_time_pref, max_study_time, max_timeblock))
