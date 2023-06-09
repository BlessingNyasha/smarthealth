from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django import forms
from django.contrib import messages
from .predict import predictly
from .predict import prediction
from .new import tryout 
from .models import *
import time
import re
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .forms import ContactForm
import matplotlib.pyplot as plt
import serial
from django.views.decorators.csrf import csrf_exempt
from django.forms import ModelChoiceField
from smarthealth.models import MedicalRecord
from smarthealth.forms import MedicalRecordForm
from .forms import ContactForm



# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else: 
            messages.info(request, 'invalid credentials')
            return redirect('index')
    else: 
        
        
        return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname= request.POST['lname']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        age = request.POST['age']
        sex = request.POST['sex']
        address = request.POST['address']
        email = request.POST['email']
        dob = request.POST['dob']
        allergies = ""
        
        keywords = ['allergic rhinitis(hay fever)','Asthma','food allegies','insect allegies','drug allegies']
        post_symptoms = []
        for key in keywords:
            post_symptom = request.POST.get(key)
            if post_symptom =="on":

                post_symptoms.append(key)
                
                allergies = allergies + " " + key
                print(post_symptom)
                
        
        
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif len(password) < 9:
                messages.info(request, 'Password Too Short')
                return redirect('register')
            elif not re.search("[A-Z]", password):
                messages.info(request, 'Password Must contain at least one uppercase letter')
                return redirect('register')
            elif not re.search("[a-z]", password):
                messages.info(request, 'Password Must contain at least one lowercase letter')
                return redirect('register')
            elif not re.search("[0-9]", password):
                messages.info(request, 'Password Must contain at least one digit')
                return redirect('register')
            elif not re.search("[!@#$%^&*()_+-=]", password):
                messages.info(request, 'Password Must contain at least one special character')
                return redirect('register')
            else:
                user= User.objects.create_user(username=username, password=password, first_name=fname ,last_name=lname )
                user.save();
                patient = Patient.objects.create(user=user, dob=dob, age=age, sex=sex, address=address, email=email)
                patient.save()
                patientspecial = PatientSpecial.objects.create(allergies=allergies, patient=patient)
                patientspecial.save()
                messages.info(request, 'Registered Successfully')
                return redirect('index')
        else:
            messages.info(request, 'password does not match')
            return redirect('register')
    else:
        keywords = ['allergic rhinitis(hay fever)','Asthma','food allergies','insect allergies','drug allegies']
        context = {'keywords':keywords}
        return render(request, 'register.html', context)
        
                
       
def home(request):
   # user_id = request.user.id
   # records = MedicalRecord.objects.get(id=user_id)
    #if request.method == 'POST':
    #    username = request.POST['username']
     #   password = request.POST['password']
        
       # user = auth.authenticate(username=username,password=password)
      #  if user is not None:
      #      auth.login(request, user)
       #     return redirect('home')
       # else: 
         #   messages.info(request, 'invalid credentials')
          #  return redirect('login')
   # else: 
        
      # Get the logged in user
    user = request.user

    # Get the medical records for that user
    medical_records = MedicalRecord.objects.filter(user=user)

    record = None
    form = MedicalRecordForm(request.POST or None)   
    
    if request.method == "POST":
        # Get the selected record type from the form
        record_type = request.POST.get("record_type")
          
        # Filter records by that type  
        records = medical_records.filter(record_type=record_type)
        
        # Get the first record, if any 
        if records.exists():
            record = records.first
            
    context = {
        'medical_records': medical_records,  
        'form': form, 
        'record': record
    }
    
    return render(request, "home.html", context)




def ecg(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('ecg')
        else: 
            messages.info(request, 'invalid credentials')
            return redirect('home')
    else: 
        return render(request,'ecg.html')
    

    
def lung(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('lung')
        else: 
            messages.info(request, 'invalid credentials')
            return redirect('home')
    else: 
    
        return render(request,'lung.html')


def faq(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('faq')
        else: 
            messages.info(request, 'invalid credentials')
            return redirect('home')
    else: 
        
        
        return render(request,'faq.html')
    

def results(request):
    if request.method == 'POST':
        
        cps = request.POST['cps']
        bpm = request.POST['bpm']
        ecg = request.POST['ecg']
        heartrate = request.POST['heartrate']
        angina = request.POST['angina']
        oldpeak = request.POST['oldpeak']
        slope = request.POST['slope']
        vessel = request.POST['vessel']
        thal = request.POST['thal']
        
        patient = Patient.objects.get(user=request.user)
        
        age = patient.age
        
        sex = patient.sex
        
        


        input_data = (int(age),int(sex),int(cps),int(bpm),int(ecg),int(heartrate),int(angina),int(oldpeak),int(slope),int(vessel),int(thal))
        
        result = predictly(input_data)
        
        print(result)
        
        context = {'result':result}

        
        return render(request,'results.html', context)
        
def resultspi(request):
    if request.method == 'POST':
        fev = request.POST['fev']
        fvc = request.POST['fvc']
        
        patient = Patient.objects.get(user=request.user)
        
        age = patient.age
        
        sex = patient.sex
        
       
        

        input_data = (int(age),int(sex),int(fev),int(fvc))
        
        resultspi = prediction(input_data)
        
        print(resultspi)
        
        context = {'resultspi':resultspi}

        
        return render(request, 'resultspi.html', context)
    
    
    context=0
	       
         
def read(request):
   
   if request.method == 'POST':
    
         print("================================")
         print(int(request.POST['command']))
         
         print("================================")
         print('here')
         command = request.POST['command']
         
         ser = serial.Serial('COM4', 115200,parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            timeout=5)
         
         time.sleep(2)
         ser.write(command.encode('utf-8'))
         
         new_values = ""
         
         time.sleep(3)
         
         while ser.in_waiting:
            data = ser.readline()
            decoded_values = str(data[0:len(data)].decode("utf-8"))
            
            new_values = new_values + decoded_values
            
            
         
         print(new_values)
         patient = Patient.objects.get(id=request.user.id)
         
         if command == '1':
            records= MedicalRecord.objects.create(user=request.user, patient=patient, temp=new_values)
            records.save()
         elif command == '2':
            records= MedicalRecord.objects.create(user=request.user, patient=patient, bpm=new_values)
            records.save()
         elif command == '3':
            records= MedicalRecord.objects.create(user=request.user, patient=patient, ecg=new_values)
            records.save()
            
            data = [int(x) for x in new_values.split(',')]
            chart_data = {'labels': list(range(len(data))), 'data': data}
            context = {'chart_data': chart_data}
            
         elif command == '4':
            records= MedicalRecord.objects.create(user=request.user, patient=patient, spirometry=new_values)
            records.save()
         
         context = {'new_values':new_values}
         return render(request,'read.html', context)
   else:
       
        ser = serial.Serial('COM4', 115200, timeout=5)
        while True:
            
            data = ser.readlines()
            data_str = b' ,'.join(data)
            decoded_values = str(data_str[0:len(data_str)].decode("utf-8").strip())
            print (decoded_values)
            
          
            
            context = {'decoded_values':decoded_values}
            return render(request,'read.html',context)

def calculate_dividend(patient_age, patient_sex):
    
    
    # Calculate the dividend based on the patient's age and sex
    if patient_sex == '0':
        if patient_age >= 20 and patient_age < 25:
            return 2.90
        elif patient_age >= 25 and patient_age < 30:
            return 2.78
        elif patient_age >= 30 and patient_age < 35:
            return 2.55
        elif patient_age >= 35 and patient_age < 40:
            return 2.50
        elif patient_age >= 40 and patient_age < 45:
            return 2.46
        elif patient_age >= 45 and patient_age < 50:
            return 2.40
        elif patient_age >= 50 and patient_age < 55:
            return 2.36
        elif patient_age >= 60 and patient_age < 65:
            return 2.29
        else:
            return 2.00 # Return 2.00 if the patient's age is not in the appropriate range for males
    elif patient_sex == '1':
        if patient_age >= 20 and patient_age < 25:
            return 2.72
        elif patient_age >= 25 and patient_age < 30:
            return 2.64
        elif patient_age >= 30 and patient_age < 35:
            return 2.58
        elif patient_age >= 35 and patient_age < 40:
            return 2.53
        elif patient_age >= 40 and patient_age < 45:
            return 2.49
        elif patient_age >= 45 and patient_age < 50:
            return 2.45
        elif patient_age >= 50 and patient_age < 55:
            return 2.41
        elif patient_age >= 60 and patient_age < 65:
            return 2.35
        else:
            return 2.00 # Return 0 if the patient's age is not in the appropriate range for females
    else:
        return 0.0 # Return 0 if the patient's sex is not recognized

from django.shortcuts import render, redirect
from .models import SpirometryRecord

def spirometry(request):
    patient = Patient.objects.get(user=request.user)
        
    age = patient.age
        
    sex = patient.sex
    
    if request.method == 'POST':
        ffev = float(request.POST['ffev'])
        ffvc = float(request.POST['ffvc'])  
        print("here")
        dividend = calculate_dividend(patient.age, patient.sex)
        
        tfev = ffev / dividend *100
        tfvc = ffvc / dividend  *100     
        fve_fev = (tfev / tfvc) * 100  
        
        lung = SpirometryRecord(user=request.user, patient=patient, 
                              fev=tfev, fvc=tfvc, fve_fev=fve_fev) 
        lung.save()  
        
        context = {
         'fev': tfev, 
         'fvc': tfvc,  
         'fve_fvc': fve_fev
       }  
       
       # Redirect to the 'lung.html' page and pass the context dictionary
        return render(request, 'lung.html', context)
      
    else:
       context = {}
      
    return render(request, 'spirometry.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'Message from your website'
            
            # Send email using send_mail function
            try:
                send_mail(
                    subject,
                    f"Name: {name}\nEmail: {email}\n\nMessage: {message}",
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False,
                )
                return JsonResponse({'success': True})
            except:
                return JsonResponse({'success': False})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def doctors(request, ):
    doctor = get_object_or_404(Doctor)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'Message from your patient: {}'.format(name)
            message = 'From: {}\nEmail: {}\n\n{}'.format(name, email, message)
            send_mail(subject, message, email, [doctor.email])
            return render(request, 'contact.html')
    else:
        form = ContactForm(initial={'message': "Dear Dr. {},\n\n".format(doctor.name)})
    return render(request, 'doctors.html', {'form': form})