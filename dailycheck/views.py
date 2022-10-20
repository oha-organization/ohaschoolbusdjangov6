import datetime

from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import School, Person, Bus, Student, Attendance, Signature

# General data for easy implementation
school = School.objects.get(id=1)
teacher = Person.objects.get(id=1)


def home(request):
    context = {"school": school, "teacher": teacher}
    return render(request, "dailycheck/home.html", context)


def school_list(request):
    context = {"school_list": School.objects.all()}
    return render(request, "dailycheck/school_list.html", context)


def attendance_choose(request):
    # Show menu to Choose bus, date, direction
    # School and user comes automatic with session
    context = {"bus_list": Bus.objects.all(), "today": datetime.date.today()}
    return render(request, "dailycheck/attendance_choose.html", context)


def attendance_get(request):
    bus = get_object_or_404(Bus.objects.all(), id=request.POST.get("bus"))
    chosen_date = request.POST.get("chosen_date")
    direction = request.POST.get("direction")
    student_list = get_list_or_404(Student.objects.all(), bus=bus)

    # Check and get attendance table for chosen date if there was a student record
    student_already_absent_list = Student.objects.filter(
        attendance__school=school,
        attendance__check_date=chosen_date,
        attendance__direction=direction,
    )

    student_list_count = len(student_list)

    context = {
        "bus": bus,
        "chosen_date": chosen_date,
        "direction": direction,
        "student_list": student_list,
        "student_list_count": student_list_count,
        "student_already_absent_list": student_already_absent_list,
    }
    return render(request, "dailycheck/attendance_get.html", context)


def attendance_save(request):
    """Show saved result"""
    chosen_date = request.POST.get("chosen_date")
    bus = request.POST.get("bus")
    direction = request.POST.get("direction")
    absent_list = request.POST.getlist("absent_list")
    student_list_count = request.POST.get("student_list_count")
    created_at = datetime.datetime.now()

    if request.method == "POST":
        for student in absent_list:
            Attendance.objects.update_or_create(
                school=school,
                check_date=chosen_date,
                direction=direction,
                student_id=student,
            )

        # Call the Signature model and sign
        Signature.objects.update_or_create(
            school=school,
            bus_id=1,
            check_date=chosen_date,
            direction=direction,
            defaults={
                "absent_count": len(absent_list),
                "actual_count": student_list_count,
                "teacher_id": 1,
            },
        )

    context = {
        "school": school,
        "bus": bus,
        "chosen_date": chosen_date,
        "direction": direction,
        "absent_list_count": len(absent_list),
        "student_list_count": student_list_count,
        "teacher": teacher,
        "created_at": created_at,
    }
    return render(request, "dailycheck/attendance_save.html", context)
