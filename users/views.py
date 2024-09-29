from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import AlangilanUsers
from .forms import AdminRegistrationForm, StudentRegistrationForm

def admin_registration(request):
  if request.method == "POST":
    form = AdminRegistrationForm(request.POST, request.FILES)
    if form.is_valid():
      user = form.save()
      messages.success(request, "Admin Registration Successful! You Can Now Log In.")
      # login(request, user)
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
      # login(request, user)
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
          return redirect('users:admin_dashboard')  # Update this with your admin dashboard URL
        elif user.role == 'student':
          return redirect('users:student_home')  # Update this with your student dashboard URL
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
  return render(request, "users/admin/profile.html")

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