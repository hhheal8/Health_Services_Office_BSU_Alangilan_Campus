from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def admin_registration(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      login(request, form.save())
      # return redirect('users:user_login') 
  else:
    form = UserCreationForm()
  
  # return render(request, 'users/admin_registration.html', { 'form': form })

def student_registration(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      login(request, form.save())
      # return redirect('users:user_login') 
  else:
    form = UserCreationForm()
  
  # return render(request, 'users/student_registration.html', { 'form': form })

def user_login(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      login(request, form.get_user())
      # return redirect("posts:list")
  else:
    form = AuthenticationForm()
  # return render(request, 'users/login.html', { 'form': form })

def user_logout(request):
  if request.method == "POST":
    logout(request)
    # return redirect("homepage")

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