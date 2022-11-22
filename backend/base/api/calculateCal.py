import calendar
import csv
import datetime


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
    winter_list = {}
    year = 2023
    for month1 in range(1, 5):
        final_dict = {}
        num_days = calendar.monthrange(year, month1)[1]
        days = [datetime.date(year, month1, day) for day in range(1, num_days + 1)]
        for day in days:
            final_dict[day] = [None] * 24
        winter_list[month1] = final_dict
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
    winter_list = winter_list_generator()
    data = read_mock_data(File_name)
    for event in data:
        event_name = get_event_name(event)
        event_start_time = get_event_start_time(event)
        event_end_time = get_event_end_time(event)
        event_days = get_event_days(event)
        dates = get_dates_for_weekday_name(event_days)
        for date in dates:
            for i in range(event_start_time, event_end_time + 1):
                winter_list[date.month][date][i] = event_name
    return winter_list


# Press the green button in the gutter to run the script.

# events={[
#             { title: ' event 1', date: '2022-11-01', display: 'block', start: '2022-11-01T10:30:00' },
#             { title: 'event 2', date: '2022-11-02' },
#             { title: 'testEvent', date: '2022-11-22',display: 'block', start: '2022-11-22T09:00:00', end: '2022-11-22T11:30:00' },
#             ]}

def convert_winter_calender_to_dict_list(winter_calender: dict) -> list:
    final_list = []
    for month in winter_calender:
        for date in winter_calender[month]:
            for hour in range(0, 24):
                if winter_calender[month][date][hour] is not None:
                    final_list.append({
                        "title": winter_calender[month][date][hour],
                        "date": str(date),
                        "display": "block",
                        "start": str(date) + "T" + str(hour) + ":00:00",
                        "end": str(date) + "T" + str(hour + 1) + ":00:00"
                    })
    return final_list


def generate_events(File_name: str) -> list:
    # study_preference, maximum_study_time, study_days_not_available = user_input('data.csv')
    # year_list = winter_list_generator()
    a = populate_winter_calendar_with_lecture_events(File_name)
    b = convert_winter_calender_to_dict_list(a)
    return b
