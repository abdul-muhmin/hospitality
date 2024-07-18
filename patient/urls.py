from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.patient_login, name='login'),
    path('logout/', views.patient_logout, name='logout'),
    path('book_appointment/', views.book_appointment, name='book_appointment'),
    path('health_resources/', views.health_resources, name='health_resources'),
    path('appointments/', views.all_appointments, name='all_appointments'),
    path('appointments/update/<int:appointment_id>/', views.update_appointment, name='update_appointment'),
    path('appointments/delete/<int:appointment_id>/', views.delete_appointment, name='delete_appointment'),
    path('doctors_lsit/', views.doctors_list, name='doctors_list'),
    path('register_doctor/', views.register_doctor, name='register_doctor'),
    path('doctor_login/', views.doctor_login, name='doctor_login'),
    path('doctor_logout/', views.doctor_logout, name='doctor_logout'),
    path('', views.firstpage, name='firstpage'),


]
