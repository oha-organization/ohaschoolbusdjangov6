# Generated by Django 4.1.2 on 2022-10-17 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "dailycheck",
            "0002_signature_unique_signature_with_school_bus_date_and_direction",
        ),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="signature",
            name="unique_signature_with_school_bus_date_and_direction",
        ),
        migrations.AlterField(
            model_name="signature",
            name="direction",
            field=models.CharField(
                choices=[("1", "Coming"), ("2", "Leaving")], max_length=1
            ),
        ),
        migrations.AlterUniqueTogether(
            name="signature",
            unique_together={("school", "bus", "check_date", "direction")},
        ),
    ]
