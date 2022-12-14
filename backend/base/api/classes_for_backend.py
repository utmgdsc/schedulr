import datetime
import math


class Assignment:
    def __init__(self, name: str, prep: int, weight: int, due: datetime.date):
        self.name = name
        self.preptime = prep
        self.prep_days = prep + 1
        self.start_datetime = due - datetime.timedelta(days=self.prep_days)
        self.duedate = due
        self.work_per_day = math.ceil(prep / self.prep_days)
        self.ROI = weight / self.preptime


class Timeslot:
    def __init__(self, ag: Assignment):
        self.ag = ag
        self.ROI = ag.ROI
        self.name = ag.name
        self.start_datetime = ag.start_datetime
        self.duedate = ag.duedate
        self.prep_days = ag.prep_days