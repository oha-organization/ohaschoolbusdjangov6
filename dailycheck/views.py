import datetime

from django.core import serializers
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.urls import reverse

from .models import School, Person, Bus, Student, Attendance, Signature

# General data for easy implementation
teacher = Person.objects.get(id=1)


def home(request):
    return redirect("dailycheck:school-list")


def school_list(request):
    context = {"school_list": School.objects.all()}
    return render(request, "dailycheck/school_list.html", context)


def attendance_choose(request, school_id):
    # Show menu to Choose bus, date, direction
    # School and user comes automatic with session
    request.session["school_id"] = school_id
    school = get_object_or_404(School.objects.all(), id=school_id)
    bus_list = Bus.objects.filter(school=school)
    context = {"bus_list": bus_list, "today": datetime.date.today()}
    return render(request, "dailycheck/attendance_choose.html", context)


def attendance_get(request):
    school = get_object_or_404(School.objects.all(), id=request.session["school_id"])
    bus = get_object_or_404(Bus.objects.all(), id=request.POST.get("bus"))
    check_date = request.POST.get("check_date")
    direction = request.POST.get("direction")
    student_list = Student.objects.filter(bus=bus)

    # Get or create new signature
    # fields = ["school", "bus", "check_date", "direction"],
    signature, created = Signature.objects.get_or_create(
        school=school,
        bus=bus,
        direction=direction,
        check_date=check_date,
        defaults={"teacher": teacher},
    )

    request.session["signature_id"] = signature.id

    # If signature is already exist get unattended student list
    student_already_absent_list = []
    if not created:
        student_already_absent_list = Student.objects.filter(
            attendance__signature=signature
        )

    context = {
        "student_list": student_list,
        "student_already_absent_list": student_already_absent_list,
        "signature": signature,
    }
    return render(request, "dailycheck/attendance_get.html", context)


def attendance_save(request):
    """Save attendance logic"""
    if request.method == "POST":
        student_absent_list = request.POST.getlist("student_absent_list")

        # Delete all attendance for signature
        signature = Signature.objects.get(id=request.session["signature_id"])
        Attendance.objects.filter(signature=signature).delete()

        # Add absent students to Attendance
        for student in student_absent_list:
            Attendance.objects.create(signature=signature, student_id=student)

        # Touch Signature Model for update to signed_at field
        signature.is_signed = True
        signature.save()

        # return redirect("dailycheck:signature-detail", signature.id)
        return redirect("dailycheck:attendance-save-done")


def attendance_save_done(request):
    signature = get_object_or_404(
        Signature.objects.all(), id=request.session["signature_id"]
    )
    context = {"signature": signature}
    return render(request, "dailycheck/attendance_save_done.html", context)


def signature_detail(request, signature_id):
    signature = get_object_or_404(Signature.objects.all(), id=signature_id)
    context = {"signature": signature}
    return render(request, "dailycheck/signature_detail.html", context)
