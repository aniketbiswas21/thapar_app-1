# Generated by Django 3.0.8 on 2020-07-29 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acad', '0007_semester'),
        ('timetable', '0006_auto_20200729_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offlineclass',
            name='batch',
        ),
        migrations.AddField(
            model_name='offlineclass',
            name='batch',
            field=models.ManyToManyField(to='acad.Batch'),
        ),
        migrations.RemoveField(
            model_name='onlineclass',
            name='batch',
        ),
        migrations.AddField(
            model_name='onlineclass',
            name='batch',
            field=models.ManyToManyField(to='acad.Batch'),
        ),
    ]
