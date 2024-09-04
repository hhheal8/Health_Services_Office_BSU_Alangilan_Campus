from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import UserAdmin, UserStudent
from .forms import UserAdminRegistration, UserStudentRegistration

UserAdmin = get_user_model()

def admin_registration(request):
  if request.method == "POST":
    form = UserAdminRegistration(request.POST, request.FILES)
    if form.is_valid():
      user = form.save(commit=False)
      user.set_password(form.cleaned_data["password"])
      user.is_staff = True
      user.is_superuser = True
      user.save()
      messages.success(request, "Admin Registration Succesful! You Can Now Log In.")
      login(request, user)
      return redirect("users:user_login")
    else:
      messages.error(request, "Invalid Input! Please Try Again.")
      return redirect("users:admin_registration")
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
      user.is_superuser = False 
      user.save()
      messages.success(request, "Student Registration Successful! You Can Now Log In.")
      login(request, user)
      return redirect("users:user_login")
    else:
      messages.error(request, "Invalid Input! Please Try Again.")
      return redirect("users:student_registration")
  else:
    form = UserStudentRegistration()
  return render(request, "users/student_registration.html", {"form": form})

def user_login(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    role = request.POST.get('role')

    print(f"Login attempt - Username: {username}, Role: {role}")

    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      print(f"Authenticated User: {user.username}, is_staff: {user.is_staff}")
      if (role == 'admin' and user.is_staff) or (role == 'student' and not user.is_staff):
        login(request, user)
        if role == 'admin':
          return redirect(reverse('users:admin_dashboard'))
        if role == 'student':
          return redirect('users:student_home')
      else:
        print("Role mismatch")  
        messages.error(request, "You don't have the necessary permissions for the selected role.")
    else:
      print("Authentication failed")  
      messages.error(request, "Invalid username or password.")
  
    return redirect('users:user_login')
  else:
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
  if not request.user.is_staff:
    messages.error(request, "You are not authorized to view this page.")
    return redirect("/")
  return render(request, "users/student/home.html")