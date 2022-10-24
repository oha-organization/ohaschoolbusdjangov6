from django.urls import path
from . import views


app_name = "dailycheck"
urlpatterns = [
    path("", views.home, name="home"),
    path("school/", views.school_list, name="school-list"),
    path(
        "attendance-choose/<int:school_id>/",
        views.attendance_choose,
        name="attendance-choose",
    ),
    path("attendance-get/", views.attendance_get, name="attendance-get"),
    path("attendance-save/", views.attendance_save, name="attendance-save"),
    path(
        "attendance-save-done/", views.attendance_save_done, name="attendance-save-done"
    ),
    path(
        "signature/<int:signature_id>/", views.signature_detail, name="signature-detail"
    ),
]
