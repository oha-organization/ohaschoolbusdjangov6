# Generated by Django 4.1.2 on 2022-10-23 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Bus",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bus_number", models.CharField(max_length=255)),
                ("capacity", models.IntegerField()),
                ("plate", models.CharField(max_length=11)),
            ],
            options={
                "ordering": ["bus_number"],
            },
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("post_code", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="District",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dailycheck.city",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Grade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("level", models.CharField(max_length=255)),
                ("branch", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ["level"],
            },
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("username", models.CharField(max_length=255)),
                ("password", models.CharField(max_length=255)),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("1", "Admin"),
                            ("2", "Manager"),
                            ("3", "Teacher"),
                            ("4", "Standard"),
                        ],
                        default="3",
                        max_length=1,
                    ),
                ),
            ],
            options={
                "ordering": ["username"],
            },
        ),
        migrations.CreateModel(
            name="School",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("code", models.IntegerField()),
                (
                    "address_detail",
                    models.CharField(blank=True, max_length=512, null=True),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "city",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dailycheck.city",
                    ),
                ),
                (
                    "district",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dailycheck.district",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Village",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dailycheck.school",
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                (
                    "bus",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="dailycheck.bus"
                    ),
                ),
                (
                    "grade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dailycheck.grade",
                    ),
                ),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dailycheck.school",
                    ),
                ),
                (
                    "village",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dailycheck.village",
                    ),
                ),
            ],
            options={
                "ordering": ["first_name"],
            },
        ),
        migrations.CreateModel(
            name="Signature",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("check_date", models.DateField()),
                (
                    "direction",
                    models.CharField(
                        choices=[("coming", "Coming"), ("leaving", "Leaving")],
                        max_length=7,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("signed_at", models.DateTimeField(auto_now=True)),
                (
                    "bus",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="dailycheck.bus"
                    ),
                ),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dailycheck.school",
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dailycheck.person",
                    ),
                ),
            ],
            options={
                "ordering": ["-check_date"],
            },
        ),
        migrations.AddField(
            model_name="person",
            name="school",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dailycheck.school"
            ),
        ),
        migrations.AddField(
            model_name="grade",
            name="school",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dailycheck.school"
            ),
        ),
        migrations.CreateModel(
            name="Driver",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dailycheck.school",
                    ),
                ),
            ],
            options={
                "ordering": ["first_name"],
            },
        ),
        migrations.AddField(
            model_name="bus",
            name="driver",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="dailycheck.driver",
            ),
        ),
        migrations.AddField(
            model_name="bus",
            name="school",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dailycheck.school"
            ),
        ),
        migrations.AddField(
            model_name="bus",
            name="village",
            field=models.ManyToManyField(to="dailycheck.village"),
        ),
        migrations.CreateModel(
            name="Attendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "signature",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dailycheck.signature",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dailycheck.student",
                    ),
                ),
            ],
            options={
                "ordering": ["-signature"],
            },
        ),
        migrations.AddConstraint(
            model_name="signature",
            constraint=models.UniqueConstraint(
                fields=("school", "bus", "check_date", "direction"),
                name="unique_signature_with_school_bus_date_and_direction",
            ),
        ),
        migrations.AddConstraint(
            model_name="attendance",
            constraint=models.UniqueConstraint(
                fields=("student", "signature"),
                name="unique_attendance_with_student_and_signature",
            ),
        ),
    ]
