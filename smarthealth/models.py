from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')
    address = models.CharField(max_length=200, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=200, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'Patient {self.user.username}'

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctors')
    doctor_id = models.CharField(max_length=200, null=True)
    speciality = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    basedLocation = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'Doctor {self.user.username}'


class PatientSpecial(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='specialties')
    allergies = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'PatientSpecialty {self.allergies}'


class MedicalRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='medical_records')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    dateOfLastCheckUp = models.DateField(null=True, default=None)
    temp = models.CharField(max_length=200, null=True, blank=True)
    bpm = models.CharField(max_length=200, null=True, blank=True)
    spirometry = models.CharField(max_length=200,null=True, blank=True)
    spirometer = models.CharField(max_length=200, null=True, blank=True)
    ecg = models.CharField(max_length=200, null=True, blank=True)
    reference = models.CharField(max_length=200, null=True, blank=True)
    record_type = models.CharField(max_length=20, choices=[('temp', 'temp'), ('bpm', 'bpm'), ('spirometry', 'spirometry'), ('ecg', 'ecg')], null=False, blank=False, default='temp')

    def __str__(self):
        return f'MedicalRecord {self.user.username} - {self.get_record_type_display()}'

    class Meta:
        ordering = ['-dateOfLastCheckUp']


class SpirometryRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='spirometry_records')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='spirometry_records', null=True)
    fev = models.FloatField(null=True, blank=True)
    fvc = models.FloatField(null=True, blank=True)
    fve_fev = models.FloatField(null=True, blank=True)
    spirometer = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'SpirometryRecord {self.user.username}'