# Generated by Django 4.2.5 on 2023-10-12 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0008_postpreparationnote_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpreparationnote',
            name='preparation_confirmation',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Has patient confirmed the receival of post preparation measures?'),
        ),
    ]