# Generated by Django 3.1.7 on 2021-04-09 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tdapp', '0003_userprofileinfo_subject_taught'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='room_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userprofileinfo',
            name='subject_taught',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
