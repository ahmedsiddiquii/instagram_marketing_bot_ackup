# Generated by Django 4.1.4 on 2022-12-23 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("insta", "0002_alter_comments_user_email"),
    ]

    operations = [
        migrations.CreateModel(
            name="Time",
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
                ("from_time", models.CharField(default=None, max_length=200)),
                ("to_time", models.CharField(default=None, max_length=200)),
            ],
        ),
        migrations.RemoveField(model_name="details", name="from_time",),
        migrations.RemoveField(model_name="details", name="to_time",),
    ]
