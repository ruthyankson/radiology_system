# Generated by Django 4.2.5 on 2023-10-19 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0015_alter_imagerejectreasons_imaging_record_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagerequestapproval',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patients.patient'),
        ),
        migrations.AlterField(
            model_name='imagerequestapproval',
            name='approval',
            field=models.CharField(choices=[('Approved', 'Approved'), ('Unapproved', 'Unapproved')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='imagerequestapproval',
            name='image_request',
            field=models.UUIDField(null=True),
        ),
    ]
