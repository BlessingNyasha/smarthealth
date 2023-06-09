from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(PatientSpecial)
admin.site.register(MedicalRecord)
admin.site.register(SpirometryRecord)