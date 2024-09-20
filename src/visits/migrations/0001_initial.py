# Generated by Django 5.0.9 on 2024-09-15 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PageVisit",
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
                ("time_stamp", models.DateTimeField(auto_created=True)),
                ("page_visit", models.TextField(blank=True)),
            ],
        ),
    ]
