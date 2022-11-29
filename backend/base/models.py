from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
     body = models.TextField()
     user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)


class Tcourse(models.Model):
    course_id = models.CharField(max_length=20, primary_key=True, null=False, default="default")

    
class Tcourseevent(models.Model):
    course_event_id = models.BigAutoField(primary_key=True)
    course_id = models.ForeignKey(Tcourse, models.CASCADE, blank=True, null=True)
    course_event_name = models.CharField(max_length=200, blank=True, null=True)
    course_event_datetime = models.DateTimeField(blank=True, null=True)
    course_event_preptime = models.IntegerField(blank=True, null=True)
    course_event_weightage = models.IntegerField(blank=True, null=True)
    course_event_type = models.CharField(max_length=50, blank=True, null=True)
    course_event_repeat = models.IntegerField(blank=True, null=True)
    course_event_weekday = models.CharField(max_length=50, blank=True, null=True)


class Tcourseclass(models.Model):
    course_class_id = models.BigAutoField(primary_key=True)
    course_id = models.ForeignKey(Tcourse, models.CASCADE, blank=True, null=True)
    course_class_name = models.CharField(max_length=200, blank=True, null=True)
    course_class_weekday = models.CharField(max_length=50, blank=True, null=True)
    course_class_duration = models.IntegerField(blank=True, null=True)
    course_class_time = models.IntegerField(blank=True, null=True)

    

class Tschedule(models.Model):
    schedule_id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    schedule_generation_reason = models.IntegerField(blank=True, null=True)

    
class Tstudent(models.Model):
    student_id = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True, unique=True)
    student_name = models.CharField(max_length=200, blank=True, null=True)
    student_email = models.CharField(max_length=200, blank=True, null=True)
    student_max_studytime = models.IntegerField(blank=True, null=True)
    student_time_pref = models.IntegerField(blank=True, null=True)
    student_max_timeblock = models.IntegerField(blank=True, null=True)
    student_day_starttime = models.IntegerField(blank=True, null=True)
    student_day_endtime = models.IntegerField(blank=True, null=True)


    
class Tstudentcourse(models.Model):
    student_course_id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    course = models.CharField(max_length=6, blank=False, null=True)

 
class Tpersonalevent(models.Model):
    personal_event_id = models.BigAutoField(primary_key=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    personal_event_name = models.CharField(max_length=200, blank=True, null=True)
    personal_event_datetime = models.DateTimeField(blank=True, null=True)
    personal_event_duration = models.IntegerField(blank=True, null=True)
    personal_event_preptime = models.IntegerField(blank=True, null=True)
    personal_event_traveltime = models.IntegerField(blank=True, null=True)

class Ttimeslot(models.Model):
    timeslot_id = models.BigAutoField(primary_key=True)
    schedule = models.ForeignKey(Tschedule, models.CASCADE, blank=True, null=True)
    timeslot_name = models.CharField(max_length=200, blank=True, null=True)
    timeslot_datetime = models.DateTimeField(blank=True, null=True)
    timeslot_duration = models.IntegerField(blank=True, null=True)
    timeslot_type = models.IntegerField(blank=True, null=True)
    course_event = models.ForeignKey(Tcourseevent, models.CASCADE, blank=True, null=True)
    personal_event = models.ForeignKey(Tpersonalevent, models.CASCADE, blank=True, null=True)



