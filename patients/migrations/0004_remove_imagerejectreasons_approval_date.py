# Generated by Django 4.2.5 on 2023-09-21 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_imagerejectreasons'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagerejectreasons',
            name='approval_date',
        ),
    ]