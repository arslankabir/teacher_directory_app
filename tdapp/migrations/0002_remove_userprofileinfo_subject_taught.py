# Generated by Django 3.1.7 on 2021-04-06 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tdapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='subject_taught',
        ),
    ]