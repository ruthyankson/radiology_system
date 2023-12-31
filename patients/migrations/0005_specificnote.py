# Generated by Django 4.2.5 on 2023-10-12 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0004_alter_patientnote_note_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecificNote',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='id')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('weight', models.FloatField()),
                ('type_of_procedure', models.CharField(choices=[('Abdomen', 'Abdomen'), ('Chest', 'Chest'), ('Knee', 'Knee'), ('Pelvis', 'Pelvis'), ('Cervical Spine', 'Cervical Spine'), ('Lumbar Spine', 'Lumbar Spine'), ('Thoracic Spine', 'Thoracic Spine')], max_length=50)),
                ('pre_procedure_bp_systolic', models.IntegerField(verbose_name='Pre Procedure BP (Systolic [mm Hg])')),
                ('pre_procedure_bp_diastolic', models.IntegerField(verbose_name='Pre Procedure BP (Diastolic [mm Hg])')),
                ('pre_pulse', models.IntegerField(verbose_name='Pulse (bpm)')),
                ('start_time_of_exams', models.TimeField(auto_now=True)),
                ('end_time_of_exams', models.TimeField(auto_now=True)),
                ('volume_of_contrast', models.FloatField(verbose_name='Volume of Contrast (mL)')),
                ('flow_rate', models.FloatField(verbose_name='Flow Rate (mL/s)')),
                ('post_procedure_bp_systolic', models.IntegerField(verbose_name='Post Procedure BP (Systolic [mm Hg])')),
                ('post_procedure_bp_diastolic', models.IntegerField(verbose_name='Post Procedure BP (Diastolic [mm Hg])')),
                ('post_pulse', models.IntegerField(verbose_name='Post Pulse (bpm)')),
                ('general_comments', models.TextField(max_length=500)),
                ('note_date', models.DateTimeField(auto_now=True, verbose_name='date')),
                ('activate_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.patient')),
            ],
            options={
                'verbose_name': 'radiology note',
                'verbose_name_plural': 'radiology notes',
            },
        ),
    ]
