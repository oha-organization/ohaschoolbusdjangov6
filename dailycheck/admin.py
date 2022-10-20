from django.contrib import admin
from .models import (
    School,
    Driver,
    Bus,
    Village,
    Grade,
    Student,
    Person,
    Attendance,
    City,
    District,
    Signature,
)


# Register your models here.
admin.site.register(School)
admin.site.register(Driver)
admin.site.register(Bus)
admin.site.register(Village)
admin.site.register(Grade)
admin.site.register(Student)
admin.site.register(Person)
admin.site.register(Attendance)
admin.site.register(City)
admin.site.register(District)
admin.site.register(Signature)
