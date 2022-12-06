import calendar
import csv
import datetime
from base.models import Tcourse
from base.models import Tcourseclass
from base.models import Tcourseevent
from base.models import Tstudentcourse
import math
import random

default_mat102_lecture = "MAT102 L0101"
default_mat135_lecture = "MAT135 L0101"
default_csc108_lecture = "CSC108 L0101"


class Assignment:
    def __init__(self, name: str, prep: int, weight: int, due: datetime.datetime):
        self.name = name
        self.preptime = prep
        self.prep_days = prep + 4
        self.start_datetime = due - datetime.timedelta(days=self.prep_days)
        self.duedate = due
        self.work_per_day = math.ceil(self.prep_days / prep)
        self.ROI = weight / self.prep_days


def get_student_courses(username: int) -> list:
    student_courses = Tstudentcourse.objects.filter(student=username)
    course_list = []
    for course in student_courses:
        course_list.append(course.course)
    return course_list


def get_assignment_list(student_courses: list) -> list:
    assignment_list = []
    course_list = Tcourseevent.objects.all()
    for student_course in student_courses:
        for course in course_list:
            if student_course in course.course_event_name:
                obj = [course.course_event_name,
                       course.course_event_preptime,
                       course.course_event_weightage,
                       course.course_event_datetime, course.course_event_repeat,
                       course.course_event_weekday]
                if obj not in assignment_list:
                    assignment_list.append(obj)

    return assignment_list


def get_assignment_object_list(assignments: list) -> list:
    assignment_list = []
    for assignment in assignments:
        if assignment[4] == 1:
            if ("CSC108" in assignment[0]) or ("MAT135" in assignment[0]) or ("MAT102" in assignment[0]):
                dates_for_assignment = get_dates_for_weekday_name_fall(assignment[5])
            else:
                dates_for_assignment = get_dates_for_weekday_name_winter(assignment[5])
            for date in dates_for_assignment:
                assignment_list.append(Assignment(assignment[0], assignment[1], assignment[2], date))
        elif assignment[4] == 0:
            assignment_list.append(Assignment(assignment[0], assignment[1], assignment[2], assignment[3]))
        else:
            if ("CSC108" in assignment[0]) or ("MAT135" in assignment[0]) or ("MAT102" in assignment[0]):
                dates_for_assignment = get_dates_for_weekday_name_fall(assignment[5])
            else:
                dates_for_assignment = get_dates_for_weekday_name_winter(assignment[5])
            for i in range(0, len(dates_for_assignment), 2):
                assignment_list.append(Assignment(assignment[0], assignment[1], assignment[2], dates_for_assignment[i]))
    return assignment_list


def get_course_class_lecture_list(student_courses: list) -> list:
    course_class_list = []
    course_class_list1 = Tcourseclass.objects.all()
    for student_course in student_courses:
        for course_class in course_class_list1:
            # if course_class.course_class_name.contains(student_course):
            if student_course in course_class.course_class_name:
                course_class_list.append([title_creater(course_class.course_class_name),
                                          class_time_format_converter(str(course_class.course_class_time)),
                                          course_class.course_class_duration // 60,
                                          course_class.course_class_weekday])
    return course_class_list


def get_course_class_lecture_list_fall(course_class_lecture_list: list) -> list:
    fall_lecture_list = []
    for lecture in course_class_lecture_list:
        if (default_csc108_lecture in lecture[0]) or (default_mat135_lecture in lecture[0]) or (
                default_mat102_lecture in lecture[0]):
            fall_lecture_list.append(lecture)
    return fall_lecture_list


def get_course_class_lecture_list_winter(course_class_lecture_list: list) -> list:
    winter_lecture_list = []
    for lecture in course_class_lecture_list:
        if ("CSC148" in lecture[0]) or ("STA107" in lecture[0]) or ("MAT136" in lecture[0]):
            winter_lecture_list.append(lecture)
    return winter_lecture_list


def title_creater(course_class_name: str) -> str:
    title_name = course_class_name.split(":")
    return title_name[0] + " " + title_name[1]


#
#
def class_time_format_converter(class_time: str) -> str:
    if len(class_time) == 3:
        return "0" + class_time
    else:
        return class_time


#
#
# def user_input(File_name: str) -> tuple:
#     with open(File_name, newline='') as f:
#         reader = csv.reader(f)
#         data = list(reader)
#     study_time_preference = data[0]
#     if data[0] == "morning":
#         study_time_preference = 0
#     elif data[0] == "noon":
#         study_time_preference = 1
#     elif data[0] == "evening":
#         study_time_preference = 2
#     maximum_study_time = data[1]
#     study_days_not_available = data[2]
#     return study_time_preference, maximum_study_time, study_days_not_available
#
#
# # def fall_list_generator
#
#
# def merge_fall_and_winter(fall_list: dict, winter_list: dict) -> dict:
#     merged_list = {}
#     for key in fall_list:
#         merged_list[key] = fall_list[key]
#     for key in winter_list:
#         merged_list[key] = winter_list[key]
#     return merged_list
#
#
def fall_list_generator() -> dict:
    fall_list = {}
    year = 2022
    for month1 in range(9, 13):
        num_days = calendar.monthrange(year, month1)[1]
        days = [datetime.date(year, month1, day) for day in range(1, num_days + 1)]
        for day in days:
            fall_list[day] = [None] * 24
    return fall_list


#
#
def winter_list_generator() -> dict:
    winter_list = {}
    year = 2023
    for month1 in range(1, 5):
        num_days = calendar.monthrange(year, month1)[1]
        days = [datetime.date(year, month1, day) for day in range(1, num_days + 1)]
        for day in days:
            winter_list[day] = [None] * 24
    return winter_list


#
#
def get_dates_for_weekday_name_fall(weekday_name: str) -> list:
    year = 2022
    month = 9
    day = 9
    date = datetime.date(year, month, day)
    dates = []
    while date.year == year and date.month <= 12:
        if date.strftime("%A") == weekday_name:
            dates.append(date)
        date += datetime.timedelta(days=1)
    return dates


def get_dates_for_weekday_name_winter(weekday_name: str) -> list:
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


def populate_fall_calendar_with_fall_lectures(class_lecture_list_fall: list) -> dict:
    fall_calendar = fall_list_generator()
    for lecture in class_lecture_list_fall:
        event_name = get_event_name(lecture)
        event_start_time = get_event_start_time(lecture)
        event_end_time = get_event_end_time(lecture)
        event_days = get_event_days(lecture)
        dates = get_dates_for_weekday_name_fall(event_days)
        for date in dates:
            for i in range(event_start_time, event_end_time):
                fall_calendar[date][i] = event_name
    return fall_calendar


def convert_fall_calender_to_dict_list(fall_calendar: dict) -> list:
    final_list = []
    for date in fall_calendar:
        for hour in range(0, 24):
            if fall_calendar[date][hour] is not None:
                final_list.append({
                    "title": fall_calendar[date][hour],
                    "date": str(date),
                    "display": "block",
                    "start": str(date) + "T" + str(hour) + ":00:00",
                    "end": str(date) + "T" + str(hour + 1) + ":00:00"
                })
    return final_list


def populate_winter_calendar_with_winter_lectures(class_lecture_list_winter: list) -> dict:
    winter_calendar = winter_list_generator()
    for lecture in class_lecture_list_winter:
        event_name = get_event_name(lecture)
        event_start_time = get_event_start_time(lecture)
        event_end_time = get_event_end_time(lecture)
        event_days = get_event_days(lecture)
        dates = get_dates_for_weekday_name_winter(event_days)
        for date in dates:
            for i in range(event_start_time, event_end_time):
                winter_calendar[date][i] = event_name
    return winter_calendar


def merge_fall_and_winter(fall_list: dict, winter_list: dict) -> dict:
    merged_list = {}
    for key in fall_list:
        merged_list[key] = fall_list[key]
    for key in winter_list:
        merged_list[key] = winter_list[key]
    return merged_list


#
#
# def read_mock_data(file_name: str) -> list:
#     with open(file_name, newline='') as f:
#         reader = csv.reader(f)
#         data = list(reader)
#     return data
#
#
def get_event_name(event: list) -> str:
    return event[0]


def get_event_start_time(event: list) -> int:
    a = event[1].strip()
    return int(a[0:2])


def get_event_end_time(event: list) -> int:
    return get_event_start_time(event) + int(event[2])


def get_event_days(event: list) -> str:
    return event[3].strip()


#
#
# def populate_winter_calendar_with_lecture_events(File_name: str) -> dict:
#     winter_list = winter_list_generator()
#     data = read_mock_data(File_name)
#     for event in data:
#         event_name = get_event_name(event)
#         event_start_time = get_event_start_time(event)
#         event_end_time = get_event_end_time(event)
#         event_days = get_event_days(event)
#         dates = get_dates_for_weekday_name_winter(event_days)
#         for date in dates:
#             for i in range(event_start_time, event_end_time):
#                 winter_list[date][i] = event_name
#     return winter_list
#
#
# def convert_winter_calender_to_dict_list(winter_calender: dict) -> list:
#     final_list = []
#     for date in winter_calender:
#         for hour in range(0, 24):
#             if winter_calender[date][hour] is not None:
#                 final_list.append({
#                     "title": winter_calender[date][hour],
#                     "date": str(date),
#                     "display": "block",
#                     "start": str(date) + "T" + str(hour) + ":00:00",
#                     "end": str(date) + "T" + str(hour + 1) + ":00:00"
#                 })
#     return final_list
#
#
# def remove_days_from_winter_calendar(winter_calendar: dict, days_to_remove: list) -> tuple:
#     temp_removed_days = {}
#     for day in days_to_remove:
#         dates_to_remove = get_dates_for_weekday_name_winter(day)
#         for date in dates_to_remove:
#             temp_removed_days[date] = winter_calendar[date]
#             del winter_calendar[date]
#     return winter_calendar, temp_removed_days
#
#
# def merge_winter_calendar_with_removed_days(winter_calendar: dict, removed_days: dict) -> dict:
#     for date in removed_days:
#         winter_calendar[date] = removed_days[date]
#     return winter_calendar
#

def generate_events(student_name: str) -> list:
    student_courses = get_student_courses(student_name)
    assignment_list = get_assignment_list(student_courses)
    assignment_object_list = get_assignment_object_list(assignment_list)
    lecture_events = get_course_class_lecture_list(student_courses)
    fall_lecture_events = get_course_class_lecture_list_fall(lecture_events)
    fall_calendar = populate_fall_calendar_with_fall_lectures(fall_lecture_events)
    fall_calendar_list = convert_fall_calender_to_dict_list(fall_calendar)
    # a = generate_schedule(assignment_object_list, fall_calendar, 0, 5, 3)
    winter_lecture_events = get_course_class_lecture_list_winter(lecture_events)
    winter_calendar = populate_winter_calendar_with_winter_lectures(winter_lecture_events)
    merged_calendar = merge_fall_and_winter(fall_calendar, winter_calendar)
    merged_calendar_list = convert_fall_calender_to_dict_list(merged_calendar)
    return merged_calendar_list

