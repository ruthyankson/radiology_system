# Generated by Django 4.2.5 on 2023-10-18 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_assignment', '0004_alter_task_assigned_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='room',
            field=models.CharField(blank=True, choices=[('CT', 'CT')], max_length=255, null=True),
        ),
    ]
