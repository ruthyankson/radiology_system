# Generated by Django 4.2.5 on 2023-09-21 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('general_setup', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0002_rename_station_imagerequest_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageRejectReasons',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='id')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('approval_date', models.DateTimeField(null=True)),
                ('radiology_staff_id', models.CharField(max_length=255)),
                ('activate_date', models.DateTimeField(auto_now=True)),
                ('acquired_image_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.acquiredimagestatus')),
                ('factors', models.ManyToManyField(to='general_setup.rejectfactor')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sub_factors', models.ManyToManyField(to='general_setup.rejectsubfactor')),
            ],
            options={
                'verbose_name': 'image reject reason',
                'verbose_name_plural': 'image reject reasons',
            },
        ),
    ]