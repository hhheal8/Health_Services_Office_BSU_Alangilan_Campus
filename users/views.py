from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AdminRegistrationForm, StudentRegistrationForm, AdminProfileUpdateForm, StudentProfileUpdateForm, StudentAppointmentForm

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
    form = StudentAppointmentForm(request.POST)
    if form.is_valid():
      appointment1 = form.save(commit=False)
      appointment1.user = request.user
      appointment1.save()
      messages.success(request, "Appointment 1 is Successful.")
      return redirect("users:student_appointment2")
    else:
      messages.error(request, "Appointment 1 is not Successful.")
  else:
    form = StudentAppointmentForm()

  return render(request, "users/student/appointment-1.html", {"form": form})

@login_required
def student_appointment2(request):
  # if request.method == "POST":
  #   form = StudentAppointment2Form(request.POST)
  #   if form.is_valid():
  #     appointment2 = form.save(commit=False)
  #     appointment2.user = request.user
  #     appointment2.save()
  #     messages.success(request, "Appointment 2 is Successful.")
  #     return redirect("users:student_appointment3")
  #   else:
  #     messages.error(request, "Appointment 2 is not Successful.")
  # else:
  #   form = StudentAppointment2Form()

  return render(request, "users/student/appointment-2.html")

@login_required
def student_appointment3(request):
  return render(request, "users/student/appointment-3.html")

@login_required
def student_appointment4_form1(request):
  return render(request, "users/student/appointment-4-form1.html")

@login_required
def student_appointment4_form2(request):
  return render(request, "users/student/appointment-4-form2.html")

@login_required
def student_appointment5(request):
  return render(request, "users/student/appointment-5.html")

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