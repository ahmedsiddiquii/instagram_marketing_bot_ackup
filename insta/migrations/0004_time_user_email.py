# Generated by Django 4.1.4 on 2022-12-23 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("insta", "0003_time_remove_details_from_time_remove_details_to_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="time",
            name="user_email",
            field=models.CharField(default=None, max_length=200),
        ),
    ]