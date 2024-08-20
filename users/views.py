from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import AdminProfile

def admin_registration(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')

    if User.objects.filter(username=username).exists():
      messages.error(request, "Username already exists.")
      return redirect("users:admin_registration")
    else:
      new_user = User.objects.create_user(
        username=username,
        password=password
      )
      messages.success(request, "Username created successfully. Proceed to complete the registration.")
      return redirect("users:user_login")
  
  return render(request, "users/admin_registration.html")

def user_login(request):
  return render(request, "users/login.html")

def admin_dashboard(request):
  return render(request, "users/admin/dashboard.html")

def admin_inventory(request):
  return render(request, "users/admin/inventory.html")

def admin_profile(request):
  return render(request, "users/admin/profile.html")

def admin_student_app(request):
  return render(request, "users/admin/student-app.html")

def admin_student_history_profile(request):
  return render(request, "users/admin/student-history-sampleProfile.html")

def admin_student_history(request):
  return render(request, "users/admin/student-history.html")

def admin_student_record_profile(request):
  return render(request, "users/admin/student-record-sampleProfile.html")

def admin_student_records(request):
  return render(request, "users/admin/student-records.html")