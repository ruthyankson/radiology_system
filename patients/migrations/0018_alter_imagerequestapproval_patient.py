# Generated by Django 4.2.5 on 2023-10-19 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0017_alter_imagerequestapproval_image_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerequestapproval',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient'),
        ),
    ]
