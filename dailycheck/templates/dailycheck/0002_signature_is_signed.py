# Generated by Django 4.1.2 on 2022-10-24 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dailycheck", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="signature",
            name="is_signed",
            field=models.BooleanField(default=False),
        ),
    ]