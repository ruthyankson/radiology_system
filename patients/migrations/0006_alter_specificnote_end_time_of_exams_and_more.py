# Generated by Django 4.2.5 on 2023-10-12 15:53

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_specificnote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specificnote',
            name='end_time_of_exams',
            field=models.TimeField(default=datetime.time(15, 53, 40, 670967)),
        ),
        migrations.AlterField(
            model_name='specificnote',
            name='note_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='specificnote',
            name='start_time_of_exams',
            field=models.TimeField(default=datetime.time(15, 53, 40, 670967)),
        ),
    ]
