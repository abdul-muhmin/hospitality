from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Patient, Appointment,Doctor
from .forms import PatientRegistrationForm, LoginForm, AppointmentForm, DoctorRegistrationForm,  DoctorLoginForm

def home(request):
    patient_id = request.session.get('patient_id', None)
    context = {
        'patient_id': patient_id,
    }
    return render(request, 'patient/home.html', context)

def register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('patient:login')
    else:
        form = PatientRegistrationForm()
    return render(request, 'patient/register.html', {'form': form})

def patient_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('patient:home')
            else:
                return render(request, 'patient/login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = LoginForm()
        
    return render(request, 'patient/login.html', {'form': form})

def patient_logout(request):
    logout(request)
    return redirect('patient:login')

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient:home')  # Adjust the redirection to where you want to go after booking
    else:
        form = AppointmentForm()
    
    return render(request, 'patient/book_appointment.html', {'form': form})

def health_resources(request):
    return render(request, 'patient/health_resources.html')

@login_required
def all_appointments(request):
    appointments = Appointment.objects.all()
    context = {
        'appointments': appointments,
    }
    return render(request, 'patient/all_appointments.html', context)

@login_required
def update_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('patient:all_appointments')  # Redirect to all_appointments page after update
    else:
        form = AppointmentForm(instance=appointment)
    
    context = {
        'form': form,
        'appointment': appointment,
    }
    return render(request, 'patient/update_appointment.html', context)

@login_required
def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, id=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('patient:all_appointments')
    context = {
        'appointment': appointment,
    }
    return render(request, 'patient/delete_appointment.html', context)


def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'patient/doctors_list.html', {'doctors': doctors})



def register_doctor(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient:doctor_login')  # Redirect to doctor login page after registration
    else:
        form = DoctorRegistrationForm()
    return render(request, 'patient/register_doctor.html', {'form': form})


def doctor_login(request):
    if request.method == 'POST':
        form = DoctorLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('patient:firstpage')  # Redirect to home page after successful login
            else:
                return render(request, 'patient/doctor_login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = DoctorLoginForm()
    return render(request, 'patient/doctor_login.html', {'form': form})

def doctor_logout(request):
    logout(request)
    return redirect('patient:doctor_logout')

def firstpage(request):
    return render(request, 'patient/firstpage.html')