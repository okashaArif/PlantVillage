# Generated by Django 4.2.5 on 2023-09-25 21:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("signinapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contactform",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="contactform",
            name="user",
        ),
    ]
