# Generated by Django 4.2.5 on 2023-09-28 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_staff',
            field=models.CharField(choices=[('Allotey', 'Allotey Kwei'), ('Ama', 'Ama Maymani'), ('', ' '), ('', ' '), ('', ' '), ('', ' ')], max_length=255),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(default='some title', max_length=255),
            preserve_default=False,
        ),
    ]
