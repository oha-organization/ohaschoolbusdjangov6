# Generated by Django 4.1.2 on 2022-10-17 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "dailycheck",
            "0003_remove_signature_unique_signature_with_school_bus_date_and_direction_and_more",
        ),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="signature",
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name="signature",
            name="absent_total",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="signature",
            name="bus_total",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]