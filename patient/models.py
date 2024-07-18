from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxLengthValidator, MinLengthValidator

class PatientManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, password, **extra_fields)

class Patient(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=15)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = PatientManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'age', 'gender', 'contact']

    def __str__(self):
        return self.username

from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Appointment(models.Model):
    patient = models.ForeignKey(
        'Patient', 
        on_delete=models.CASCADE,
        verbose_name="Patient",
        help_text="Select the patient for this appointment."
    )
    doctor = models.CharField(
        max_length=100,
        verbose_name="Doctor's Name",
        help_text="Enter the name of the doctor.",
        validators=[MinLengthValidator(2, "Doctor's name must be at least 2 characters long.")]
    )
    date = models.DateField(
        verbose_name="Appointment Date",
        help_text="Enter the date of the appointment (YYYY-MM-DD)."
    )
    time = models.TimeField(
        verbose_name="Appointment Time",
        help_text="Enter the time of the appointment (HH:MM:SS)."
    )

    class Meta:
        verbose_name = "Appointment"
        verbose_name_plural = "Appointments"
        ordering = ['date', 'time']

    def __str__(self):
        return f"Appointment with Dr. {self.doctor} on {self.date} at {self.time}"




class Doctor(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    speciality = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'speciality', 'location', 'contact']


    def __str__(self):
        return self.name