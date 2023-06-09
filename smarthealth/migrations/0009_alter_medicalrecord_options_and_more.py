# Generated by Django 4.2 on 2023-06-04 15:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('smarthealth', '0008_rename_patient_medicalrecord_patient'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicalrecord',
            options={'ordering': ['-dateOfLastCheckUp']},
        ),
        migrations.RenameField(
            model_name='patientspecial',
            old_name='allegies',
            new_name='allergies',
        ),
        migrations.RemoveField(
            model_name='spirometryrecord',
            name='Patient',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='bpm',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='ecg',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_records', to='smarthealth.patient'),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='spirometry',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='temp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_records', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patient',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patientspecial',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialties', to='smarthealth.patient'),
        ),
        migrations.AlterField(
            model_name='spirometryrecord',
            name='fev',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='spirometryrecord',
            name='fvc',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='spirometryrecord',
            name='fve_fev',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='spirometryrecord',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spirometry_records', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='spirometryrecord',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spirometry_records', to='smarthealth.patient'),
        ),
    ]