from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from .models import UserAdmin, UserStudent
from .forms import UserAdminRegistration, UserStudentRegistration

def admin_registration(request):
  if request.method == "POST":
    form = UserAdminRegistration(request.POST, request.FILES)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data["password"])
      user.is_staff = True
      user.save()
      messages.success(request, "Admin Registration Succesful! You Can Now Log In.")
      login(request, user)
      return redirect("users:user_login")
    else:
      messages.error(request, "Invalid Input! Please Try Again.")
  else:
    form = UserAdminRegistration()
      
  return render(request, "users/admin_registration.html", {"form": form})

def student_registration(request):
  if request.method == "POST":
    form = UserStudentRegistration(request.POST, request.FILES)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data["password"])
      user.is_staff = False  
      user.save()
      messages.success(request, "Student Registration Successful!")
      login(request, user)
      return redirect("users:user_login")
    else:
      messages.error(request, "Invalid Input! Please Try Again.")
  else:
    form = UserStudentRegistration()
      
  return render(request, "users/student_registration.html", {"form": form})

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