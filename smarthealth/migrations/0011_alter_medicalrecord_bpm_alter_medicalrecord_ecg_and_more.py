# Generated by Django 4.2 on 2023-06-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smarthealth', '0010_alter_medicalrecord_bpm_alter_medicalrecord_ecg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecord',
            name='bpm',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='ecg',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='spirometry',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='temp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
