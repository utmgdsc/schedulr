from django.db import models

from django.contrib.auth.models import User


# Create your models here.


class Note(models.Model):

     body = models.TextField()

     user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
     

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BaseNote(models.Model):
    id = models.BigAutoField(primary_key=True)
    body = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_note'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Tcourse(models.Model):
    course_id = models.CharField(primary_key=True, max_length=10)
    course_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tCourse'


class Tcourseevent(models.Model):
    course_event_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Tcourse, models.DO_NOTHING, blank=True, null=True)
    course_event_name = models.CharField(max_length=200, blank=True, null=True)
    course_event_datetime = models.DateTimeField(blank=True, null=True)
    course_event_duration = models.IntegerField(blank=True, null=True)
    course_event_preptime = models.IntegerField(blank=True, null=True)
    course_event_traveltime = models.IntegerField(blank=True, null=True)
    course_event_weightage = models.IntegerField(blank=True, null=True)
    course_event_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tCourseEvent'


class Tpersonalevent(models.Model):
    personal_event_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Tstudent', models.DO_NOTHING, blank=True, null=True)
    personal_event_name = models.CharField(max_length=200, blank=True, null=True)
    personal_event_datetime = models.DateTimeField(blank=True, null=True)
    personal_event_duration = models.IntegerField(blank=True, null=True)
    personal_event_preptime = models.IntegerField(blank=True, null=True)
    personal_event_traveltime = models.IntegerField(blank=True, null=True)
    timeslot_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tPersonalEvent'


class Tschedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Tstudent', models.DO_NOTHING, blank=True, null=True)
    schedule_generation_reason = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tSchedule'


class Tstudent(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=200, blank=True, null=True)
    student_email = models.CharField(max_length=200, blank=True, null=True)
    student_max_studytime = models.IntegerField(blank=True, null=True)
    student_time_pref = models.IntegerField(blank=True, null=True)
    student_max_timeblock = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tStudent'


class Tstudentcourse(models.Model):
    student_course_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Tstudent, models.DO_NOTHING, blank=True, null=True)
    course = models.ForeignKey(Tcourse, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tStudentCourse'


class Ttimeslot(models.Model):
    timeslot_id = models.AutoField(primary_key=True)
    schedule = models.ForeignKey(Tschedule, models.DO_NOTHING, blank=True, null=True)
    timeslot_name = models.CharField(max_length=200, blank=True, null=True)
    timeslot_datetime = models.DateTimeField(blank=True, null=True)
    timeslot_duration = models.IntegerField(blank=True, null=True)
    timeslot_type = models.IntegerField(blank=True, null=True)
    course_event = models.ForeignKey(Tcourseevent, models.DO_NOTHING, blank=True, null=True)
    personal_event = models.ForeignKey(Tpersonalevent, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tTimeslot'

