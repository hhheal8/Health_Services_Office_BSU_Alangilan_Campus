from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import UserAppointment
from .forms import AdminRegistrationForm, StudentRegistrationForm, AdminProfileUpdateForm, StudentProfileUpdateForm, StudentAppointment1Form, StudentAppointment2Form, StudentAppointment4Form2

def admin_registration(request):
  if request.method == "POST":
    form = AdminRegistrationForm(request.POST, request.FILES)
    if form.is_valid():
      user = form.save()
      messages.success(request, "Admin Registration Successful! You Can Now Log In.")
      return redirect("users:user_login")
    else:
      messages.error(request, "Invalid Input! Please Try Again.")
      return redirect("users:admin_registration")
  else:
    form = AdminRegistrationForm()
  return render(request, "users/admin_registration.html", {"form": form})

def student_registration(request):
  if request.method == "POST":
    form = StudentRegistrationForm(request.POST, request.FILES)
    if form.is_valid():
      user = form.save()
      messages.success(request, "Student Registration Successful! You Can Now Log In.")
      return redirect("users:user_login")
    else:
      messages.error(request, "Invalid Input! Please Try Again.")
      return redirect("users:student_registration")
  else:
    form = StudentRegistrationForm()
  return render(request, "users/student_registration.html", {"form": form})

def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    role = request.POST.get('role')

    user = authenticate(request, username=username, password=password)

    if user is not None:
      if user.role == role:
        login(request, user)
        if user.role == 'admin':
          return redirect('users:admin_dashboard') 
        elif user.role == 'student':
          return redirect('users:student_home')
        else:
          messages.error(request, 'Invalid role selected for this user.')
          redirect("users:user_login")
      else:
        messages.error(request, 'Invalid username or password.')
        redirect("users:user_login")

  return render(request, 'users/login.html')

@login_required
def user_logout(request):
  logout(request)
  messages.success(request, "You have successfully logged out.")
  return redirect('index')

@login_required
def admin_dashboard(request):
  if not request.user.is_staff:
    messages.error(request, "You are not authorized to view this page.")
    return redirect("/") 

  return render(request, "users/admin/dashboard.html")

@login_required
def admin_inventory(request):
  if not request.user.is_staff:
    messages.error(request, "You are not authorized to view this page.")
    return redirect("/")
  return render(request, "users/admin/inventory.html")

@login_required
def admin_profile(request):
  if not request.user.is_staff:
    messages.error(request, "You are not authorized to view this page.")
    return redirect("/")

  if request.method == "POST":
    form = AdminProfileUpdateForm(request.POST, request.FILES, instance=request.user)
    if form.is_valid():
      form.save()
      messages.success(request, "Profile Successfully Updated.")
      return redirect("users:admin_profile")
    else:
      messages.error(request, "Profile could not be updated.")
  else:
    form = AdminProfileUpdateForm(instance=request.user)
  
  return render(request, "users/admin/profile.html", {"form": form})

@login_required
def admin_student_app(request):
  if not request.user.is_staff:
    messages.error(request, "You are not authorized to view this page.")
    return redirect("/")
  return render(request, "users/admin/student-app.html")

@login_required
def admin_student_history_profile(request):
  if not request.user.is_staff:
    messages.error(request, "You are not authorized to view this page.")
    return redirect("/")
  return render(request, "users/admin/student-history-sampleProfile.html")

@login_required
def admin_student_history(request):
  if not request.user.is_staff:
    messages.error(request, "You are not authorized to view this page.")
    return redirect("/")
  return render(request, "users/admin/student-history.html")

@login_required
def admin_student_record_profile(request):
  if not request.user.is_staff:
    messages.error(request, "You are not authorized to view this page.")
    return redirect("/")
  return render(request, "users/admin/student-record-sampleProfile.html")

@login_required
def admin_student_records(request):
  if not request.user.is_staff:
    messages.error(request, "You are not authorized to view this page.")
    return redirect("/")
  return render(request, "users/admin/student-records.html")

@login_required
def student_home(request):
  return render(request, "users/student/home.html")

@login_required
def student_appointment1(request):
  if request.method == "POST":
    form = StudentAppointment1Form(request.POST)
    if form.is_valid():
      appointment = form.save(commit=False)
      appointment.user = request.user
      appointment.appointment_date = None
      appointment.appointment_time = None
      appointment.save()  
      messages.success(request, "Appointment 1 is Successful.")
      print(f"Redirecting to step 2 with appointment_id={appointment.id}")  
      return redirect("users:student_appointment2", appointment_id=appointment.id)
    else:
      print(form.errors)  
      messages.error(request, "Appointment 1 submission failed.")
  else:
    form = StudentAppointment1Form()

  return render(request, "users/student/appointment-1.html", {"form": form})

@login_required
def student_appointment2(request, appointment_id):
  appointment = get_object_or_404(UserAppointment, id=appointment_id)
  if request.method == "POST":
    form = StudentAppointment2Form(request.POST, instance=appointment)
    if form.is_valid():
      appointment = form.save(commit=False)
      appointment.user = request.user
      appointment.save()
      messages.success(request, "Appointment 2 is Successful.")
      print(f"Redirecting to step 3 with appointment_id={appointment.id}")  
      return redirect("users:student_appointment3", appointment_id=appointment.id)
    else:
      messages.error(request, "Appointment 2 submission failed.")
  else:
    form = StudentAppointment2Form(instance=appointment)

  return render(request, "users/student/appointment-2.html", {
    "form": form,
    "appointment": appointment
  })

@login_required
def student_appointment3(request, appointment_id):
  appointment = get_object_or_404(UserAppointment, id=appointment_id)
  return render(request, "users/student/appointment-3.html", {"appointment": appointment})

@login_required
def student_appointment4_form2(request, appointment_id):
  appointment = get_object_or_404(UserAppointment, id=appointment_id)
  if request.method=="POST":
    form = StudentAppointment4Form2(request.POST, request.FILES, instance=appointment)
    if form.is_valid():
      appointment = form.save(commit=False)
      appointment.user = request.user
      appointment.save()
      messages.success(request, "Appointment 4 is Successful.")
      print(f"Redirecting to step 5 with URL: {reverse('users:student_appointment5', kwargs={'appointment_id': appointment.id})}")
      print(f"Redirecting to step 5 with appointment_id={appointment.id}")
      return redirect("users:student_appointment5", appointment_id=appointment.id)
    else:
      messages.error(request, "Appointment 4 submission failed.")
  else:
    form = StudentAppointment4Form2(instance=appointment)

  return render(request, "users/student/appointment-4-form2.html", {
    "form": form,
    "appointment": appointment
  })

@login_required
def student_appointment5(request, appointment_id):
  appointment = get_object_or_404(UserAppointment, id=appointment_id)
  return render(request, "users/student/appointment-5.html", {"appointment": appointment})

@login_required
def student_profile(request):
  if request.method == "POST":
    form = StudentProfileUpdateForm(request.POST, request.FILES, instance=request.user)
    if form.is_valid():
      form.save()
      messages.success(request, "Profile Successfully Updated.")
      return redirect("users:student_profile")
    else:
      messages.error(request, "Profile could not be updated.")
  else:
    form = StudentProfileUpdateForm(instance=request.user)

  return render(request, "users/student/profile.html", {"form": form})