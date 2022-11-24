import csv
from django.core.management import BaseCommand
from base.models import Tcourseclass, Tcourseevent, Tcourse
import datetime

class Command(BaseCommand):
    help = "Loads products and product categories from CSV file."

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    def handle(self, *args, **options):
        file_path = options["file_path"]
        # Tcourse.objects.create(course_id="MAT102")
        # Tcourse.objects.create(course_id="MAT135")
        # Tcourse.objects.create(course_id="MAT136")
        # Tcourse.objects.create(course_id="MAT137")
        # Tcourse.objects.create(course_id="CSC108")
        # Tcourse.objects.create(course_id="CSC148")
        # Tcourse.objects.create(course_id="STA107")

        with open(file_path, "r") as csv_file:
            data = list(csv.reader(csv_file, delimiter=","))
            
            for row in data[1:]:
                # Tcourseclass.objects.create(course_id=Tcourse(course_id=row[0]), course_class_name=row[1], course_class_weekday=row[2], course_class_duration=row[3],course_class_time=row[4])
                
                # if row[5] != "":
                #     Tcourseevent.objects.create(course_id=Tcourse(course_id=row[0]), course_event_name=row[1], course_event_preptime=int(row[2]), course_event_type=row[3], course_event_weightage=int(row[4]),course_event_datetime=datetime.datetime(int(row[5][0:4]),int(row[5][5:7]),int(row[5][8:10]),int(row[5][11:13])), course_event_repeat=int(row[6]), course_event_weekday=row[7])

                # else: 
                #     Tcourseevent.objects.create(course_id=Tcourse(course_id=row[0]), course_event_name=row[1], course_event_preptime=int(row[2]), course_event_type=row[3], course_event_weightage=int(row[4]), course_event_weekday=row[7])

