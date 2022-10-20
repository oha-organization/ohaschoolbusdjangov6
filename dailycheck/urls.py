from django.urls import path
from . import views


app_name = "dailycheck"
urlpatterns = [
    path("", views.home, name="home"),
    path("school/", views.school_list, name="school-list"),
    path("attendance-choose/", views.attendance_choose, name="attendance-choose"),
    path("attendance-get/", views.attendance_get, name="attendance-get"),
    path("attendance-save/", views.attendance_save, name="attendance-save"),
]
