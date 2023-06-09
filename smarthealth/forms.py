from django import forms

from smarthealth.models import MedicalRecord
from .models import Patient


class MedicalRecordForm(forms.ModelForm):
   class Meta:
        model = MedicalRecord()
       # fields = ("__all__")
       # record_type = forms.ModelChoiceField(queryset=MedicalRecord.objects.all(), empty_label=None, label='Select a medical record')
        #model = MedicalRecord
        #fields = ['temp', 'bpm', 'spirometry', 'spirometer', 'ecg', 'reference']
        #record_type = forms.ChoiceField(choices=MedicalRecord.RECORD_TYPE_CHOICES)   
        model = MedicalRecord
        fields = ['record_type']
        
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)        