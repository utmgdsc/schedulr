import calendar
import datetime
from .classes_for_backend import Assignment

from base.models import Tcourseclass
from base.models import Tcourseevent
from base.models import Tstudent
from base.models import Tstudentcourse

from .generate_schedule import generate_schedule


def get_student_courses_timings(username: int) -> list:
    student_courses = Tstudentcourse.objects.filter(student=username)
    course_list = []
    for course in student_courses:
        course_list.append(course.course + ":" + course.course_lec)
        course_list.append(course.course + ":" + course.course_tut)
    return course_list


def get_student_preferences(username: int) -> list:
    student = Tstudent.objects.filter(student_id=username)
    for student in student:
        return [student.student_time_pref, student.student_max_studytime, student.student_max_timeblock]


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


def get_assignment_list_for_fall(assignment_list: list) -> list:
    fall_assignment_list = []
    for assignment in assignment_list:
        if ("CSC108" in assignment.name) or ("MAT135" in assignment.name) or ("MAT102" in assignment.name):
            fall_assignment_list.append(assignment)
    return fall_assignment_list


def get_assignment_list_for_winter(assignment_list: list) -> list:
    winter_assignment_list = []
    for assignment in assignment_list:
        if ("CSC148" in assignment.name) or ("STA107" in assignment.name) or ("MAT136" in assignment.name):
            winter_assignment_list.append(assignment)
    return winter_assignment_list


def get_assignment_object_list(assignments: list) -> list:
    assignment_list = []
    for assignment in assignments:
        if assignment[4] == 1:
            if ("CSC108" in assignment[0]) or ("MAT135" in assignment[0]) or ("MAT102" in assignment[0]):
                dates_for_assignment = get_dates_for_weekday_name_fall(assignment[5])
            else:
                dates_for_assignment = get_dates_for_weekday_name_winter(assignment[5])
            for date in dates_for_assignment:
                if type(date) == datetime.datetime:
                    date = date.date()
                assignment_list.append(Assignment(assignment[0], assignment[1], assignment[2], date))
        elif assignment[4] == 0:
            if type(assignment[3]) == datetime.datetime:
                assignment[3] = assignment[3].date()
            assignment_list.append(Assignment(assignment[0], assignment[1], assignment[2], assignment[3]))
        else:
            if ("CSC108" in assignment[0]) or ("MAT135" in assignment[0]) or ("MAT102" in assignment[0]):
                dates_for_assignment = get_dates_for_weekday_name_fall(assignment[5])
            else:
                dates_for_assignment = get_dates_for_weekday_name_winter(assignment[5])
            for i in range(0, len(dates_for_assignment), 2):
                if type(dates_for_assignment[i]) == datetime.datetime:
                    dates_for_assignment[i] = dates_for_assignment[i].date()
                assignment_list.append(Assignment(assignment[0], assignment[1], assignment[2],
                                                  dates_for_assignment[i]))
    return assignment_list


def get_course_class_lecture_list(student_courses_timings: list) -> list:
    course_class_list = []
    course_class_list1 = Tcourseclass.objects.all()
    for student_course in student_courses_timings:
        for course_class in course_class_list1:
            if student_course in course_class.course_class_name:
                course_class_list.append([title_creater(course_class.course_class_name),
                                          class_time_format_converter(str(course_class.course_class_time)),
                                          course_class.course_class_duration // 60,
                                          course_class.course_class_weekday])
    return course_class_list


def get_lectures_for_fall(lecture_list: list) -> list:
    fall_lecture_list = []
    for lecture in lecture_list:
        if ("CSC108" in lecture[0]) or ("MAT135" in lecture[0]) or ("MAT102" in lecture[0]):
            fall_lecture_list.append(lecture)
    return fall_lecture_list


def get_lectures_for_winter(lecture_list: list) -> list:
    winter_lecture_list = []
    for lecture in lecture_list:
        if ("CSC148" in lecture[0]) or ("STA107" in lecture[0]) or ("MAT136" in lecture[0]):
            winter_lecture_list.append(lecture)
    return winter_lecture_list


def title_creater(course_class_name: str) -> str:
    title_name = course_class_name.split(":")
    return title_name[0] + " " + title_name[1]


def class_time_format_converter(class_time: str) -> str:
    if len(class_time) == 3:
        return "0" + class_time
    else:
        return class_time


def fall_list_generator() -> dict:
    fall_list = {}
    year = 2022
    for month1 in range(9, 13):
        num_days = calendar.monthrange(year, month1)[1]
        days = [datetime.date(year, month1, day) for day in range(1, num_days + 1)]
        for day in days:
            fall_list[day] = [None] * 24
    return fall_list


def winter_list_generator() -> dict:
    winter_list = {}
    year = 2023
    for month1 in range(1, 5):
        num_days = calendar.monthrange(year, month1)[1]
        days = [datetime.date(year, month1, day) for day in range(1, num_days + 1)]
        for day in days:
            winter_list[day] = [None] * 24
    return winter_list


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
    day = 7
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


def merge_fall_list_and_winter_list(fall_list: list, winter_list: list) -> list:
    merged_list = []
    for item in fall_list:
        merged_list.append(item)
    for item in winter_list:
        merged_list.append(item)
    return merged_list


def get_event_name(event: list) -> str:
    return event[0]


def get_event_start_time(event: list) -> int:
    a = event[1].strip()
    return int(a[0:2])


def get_event_end_time(event: list) -> int:
    return get_event_start_time(event) + int(event[2])


def get_event_days(event: list) -> str:
    return event[3].strip()
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

def generate_events(student_name: str) -> list:
    student_courses = get_student_courses(student_name)
    student_pref = get_student_preferences(student_name)
    student_courses_timings = get_student_courses_timings(student_name)
    assignment_list = get_assignment_list(student_courses)
    assignment_object_list = get_assignment_object_list(assignment_list)
    lecture_events = get_course_class_lecture_list(student_courses_timings)
    lectures_for_fall = get_lectures_for_fall(lecture_events)
    fall_calendar = populate_fall_calendar_with_fall_lectures(lectures_for_fall)
    assignments_for_fall = get_assignment_list_for_fall(assignment_object_list)
    
    a = generate_schedule(assignments_for_fall, fall_calendar, student_pref[0], student_pref[1], student_pref[2])
    lectures_for_winter = get_lectures_for_winter(lecture_events)
    winter_calendar = populate_winter_calendar_with_winter_lectures(lectures_for_winter)
    assignments_for_winter = get_assignment_list_for_winter(assignment_object_list)
    b = generate_schedule(assignments_for_winter, winter_calendar, student_pref[0], student_pref[1], student_pref[2])
    print("-----------------------generation done!!! :D -------------")
    return merge_fall_list_and_winter_list(a, b)
    #return convert_winter_calender_to_dict_list(fall_calendar)