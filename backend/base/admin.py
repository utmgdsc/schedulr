from django.contrib import admin

# Register your models here.
from .models import Note
from .models import Tcourse, Tcourseevent, Tpersonalevent, Tschedule, Tstudent, Ttimeslot, Tstudentcourse, Tcourseclass

admin.site.register(Note)
admin.site.register(Tcourse)
admin.site.register(Tcourseevent)
admin.site.register(Tpersonalevent)
admin.site.register(Tschedule)
admin.site.register(Tstudent)
admin.site.register(Ttimeslot)
admin.site.register(Tstudentcourse)
admin.site.register(Tcourseclass)