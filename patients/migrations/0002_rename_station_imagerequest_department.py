# Generated by Django 4.2.5 on 2023-09-21 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagerequest',
            old_name='station',
            new_name='department',
        ),
    ]