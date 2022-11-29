import calendar
import csv
import datetime
from base.models import Tcourse
from base.models import Tcourseclass
from base.models import Tcourseevent
import math


class Assignment:
    def __init__(self, name: str, prep: int, weight: int, due: datetime.datetime):
        self.name = name
        self.prep = prep + 4
        self.start_datetime = due - datetime.timedelta(days=self.prep)
        self.work_per_day = math.ceil(self.prep / prep)
        self.ROI = weight / self.prep


def get_assignment_list() -> list:
    assignment_list = []
    course_list = Tcourseevent.objects.all()
    for course in course_list:
        assignment_list.append([course.course_event_name,
                                course.course_event_preptime,
                                course.course_event_weightage,
                                course.course_event_datetime, course.course_event_repeat,
                                course.course_event_weekday])
    return assignment_list


def get_assignment_object_list(assignments: list) -> list:
    assignment_list = []
    for assignment in assignments:
        if assignment[4] == 1:
            dates_for_assignment = get_dates_for_weekday_name(assignment[5])
            for date in dates_for_assignment:
                assignment_list.append(Assignment(assignment[0], assignment[1], assignment[2], date))
        elif assignment[4] == 0:
            assignment_list.append(Assignment(assignment[0], assignment[1], assignment[2], assignment[3]))
        else:
            dates_for_assignment = get_dates_for_weekday_name(assignment[5])
            for i in range(0, len(dates_for_assignment), 2):
                assignment_list.append(Assignment(assignment[0], assignment[1], assignment[2], dates_for_assignment[i]))
    return assignment_list


def get_course_class_lecture_list() -> list:
    course_class_list = []
    course_class_list1 = Tcourseclass.objects.all()
    for course_class in course_class_list1:
        course_class_list.append([title_creater(course_class.course_class_name),
                                  class_time_format_converter(str(course_class.course_class_time)),
                                  course_class.course_class_duration // 60,
                                  course_class.course_class_weekday])
    return course_class_list


def title_creater(course_class_name: str) -> str:
    title_name = course_class_name.split(":")
    return title_name[0] + " " + title_name[1]


def class_time_format_converter(class_time: str) -> str:
    if len(class_time) == 3:
        return "0" + class_time
    else:
        return class_time


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
    # courses = Tcourse.objects.all()
    # for course in courses:
    #     name_of_course = course.course_id
    #     print(name_of_course)
    class_list = get_course_class_lecture_list()
    assignment_list = get_assignment_list()
    assignment_list_object = get_assignment_object_list(assignment_list)
    return b
