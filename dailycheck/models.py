from django.db import models
from django.urls import reverse


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=255)
    post_code = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, blank=True, null=True
    )
    address_detail = models.CharField(max_length=512, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("dailycheck:school-detail", kwargs={"pk": self.pk})


class Village(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("dailycheck:village-detail", kwargs={"pk": self.pk})


class Driver(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Bus(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, blank=True, null=True)
    bus_number = models.CharField(max_length=255)
    capacity = models.IntegerField()
    plate = models.CharField(max_length=11)
    village = models.ManyToManyField(Village)

    class Meta:
        ordering = ["bus_number"]

    def __str__(self):
        return self.bus_number


class Grade(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    level = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)

    class Meta:
        ordering = ["level"]

    def __str__(self):
        return f"{self.level}/{self.branch}"


class Student(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    # evening_bus = models.ForeignKey(Bus, on_delete=models.RESTRICT)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)

    class Meta:
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"


class Person(models.Model):
    ROLE_CHOICES = (
        ("1", "Admin"),
        ("2", "Manager"),
        ("3", "Teacher"),
        ("4", "Standard"),
    )
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default="3")

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username


class Attendance(models.Model):
    DIRECTION_CHOICES = (
        ("coming", "Coming"),
        ("leaving", "Leaving"),
    )
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    check_date = models.DateField()
    direction = models.CharField(max_length=7, choices=DIRECTION_CHOICES)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-check_date"]
        constraints = [
            models.UniqueConstraint(
                fields=["school", "check_date", "direction", "student"],
                name="unique_student_with_school_date_direction_and_student",
            )
        ]

    def __str__(self):
        return f"{self.school} | {self.check_date} | {self.direction} | {self.student}"


class Signature(models.Model):
    DIRECTION_CHOICES = (
        ("coming", "Coming"),
        ("leaving", "Leaving"),
    )
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    check_date = models.DateField()
    direction = models.CharField(max_length=7, choices=DIRECTION_CHOICES)
    absent_count = models.IntegerField(blank=True, null=True)
    actual_count = models.IntegerField(blank=True, null=True)
    teacher = models.ForeignKey(Person, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-check_date"]
        constraints = [
            models.UniqueConstraint(
                fields=["school", "bus", "check_date", "direction"],
                name="unique_signature_with_school_bus_date_and_direction",
            )
        ]

    def __str__(self):
        return (
            f"{self.school} | {self.bus} | {self.check_date} | {self.direction} | {self.absent_count} | "
            f"{self.actual_count} | {self.teacher} | {self.created_at} "
        )
