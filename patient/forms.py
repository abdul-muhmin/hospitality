from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient,Doctor
from django.contrib.auth import authenticate
from .models import Appointment


class PatientRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=255)
    age = forms.IntegerField()
    gender = forms.CharField(max_length=10)
    contact = forms.CharField(max_length=15)

    class Meta:
        model = Patient
        fields = ['username', 'name', 'age', 'gender', 'contact', 'password1', 'password2']
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid login credentials")
        return super().clean()


class AppointmentForm(forms.ModelForm):
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all(), empty_label="Select Doctor")

    class Meta:
        model = Appointment
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }        
        
class DoctorRegistrationForm(UserCreationForm):
    SPECIALITY_CHOICES = [
        ('Cardiology', 'Cardiology'),
        ('Pediatrics', 'Pediatrics'),
        ('Orthopedics', 'Orthopedics'),
        ('Dermatology', 'Dermatology'),
        ('Ophthalmology', 'Ophthalmology'),
        ('Neurology', 'Neurology'),
        ('Gynecology', 'Gynecology'),
        ('Urology', 'Urology'),
        ('ENT', 'ENT'),
        ('Oncology', 'Oncology'),
    ]

    name = forms.CharField(max_length=255)
    speciality = forms.ChoiceField(choices=SPECIALITY_CHOICES) 
    location = forms.CharField(max_length=100)
    contact = forms.CharField(max_length=15)

    class Meta:
        model = Doctor
        fields = ['username','name', 'speciality','location','contact','password1', 'password2']
        
class DoctorLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid login credentials")
        return super().clean()
