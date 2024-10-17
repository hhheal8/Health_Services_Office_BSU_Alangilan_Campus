from django import forms
from django.forms.widgets import PasswordInput
from .models import AlangilanUsers, UserAppointment
from django.core.exceptions import ValidationError

class AdminRegistrationForm(forms.ModelForm):
  password = forms.CharField(widget=PasswordInput)
    
  class Meta:
    model = AlangilanUsers
    fields = [
      'username', 'first_name', 'middle_name', 'last_name', 'suffix', 'age', 'position', 
      'sex', 'contact_number', 'telephone_number', 'email', 
      'profile_image', 'present_address', 'home_address'       
    ]

  def clean_username(self):
    username = self.cleaned_data.get('username')
    if AlangilanUsers.objects.filter(username=username).exists():
      raise ValidationError("This username is already taken.")
    return username
  
  def clean_email(self):
    email = self.cleaned_data.get('email')
    if AlangilanUsers.objects.filter(email=email).exists():
      raise ValidationError("This email is already in use.")
    return email
        
  def save(self, commit=True):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password'])
    user.role = 'admin'
    user.is_staff = True
    if commit:
      user.save()
    return user

class StudentRegistrationForm(forms.ModelForm):
  password = forms.CharField(widget=PasswordInput)
    
  class Meta:
    model = AlangilanUsers
    fields = [
      'username', 'first_name', 'middle_name', 'last_name', 'suffix', 'birth_date', 'sr_code', 
      'age', 'sex', 'contact_number', 'telephone_number', 'email', 
      'civil_status', 'gsuite', 'present_address', 'home_address', 
      'profile_image'
    ]

  def clean_username(self):
    username = self.cleaned_data.get('username')
    if AlangilanUsers.objects.filter(username=username).exists():
      raise ValidationError("This username is already taken.")
    return username
  
  def clean_email(self):
    email = self.cleaned_data.get('email')
    if AlangilanUsers.objects.filter(email=email).exists():
      raise ValidationError("This email is already in use.")
    return email
  
  def save(self, commit=True):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password'])
    user.role = 'student'
    user.is_staff = False
    if commit:
      user.save()
    return user

class AdminProfileUpdateForm(forms.ModelForm):
  class Meta:
    model = AlangilanUsers
    fields = [
      'profile_image', 'first_name', 'middle_name', 'last_name', 'position', 
      'age', 'contact_number', 'sex', 'present_address', 'email'
    ]
    widgets = {
      'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'position': forms.Select(choices=AlangilanUsers.POSITION_CHOICES),
      'age': forms.NumberInput(attrs={'class': 'form-control'}),
      'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
      'sex': forms.Select(choices=AlangilanUsers.SEX_CHOICES),
      'present_address': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'})
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['email'].required = True

class StudentProfileUpdateForm(forms.ModelForm): 
  class Meta:
    model = AlangilanUsers
    fields = [
      'profile_image', 'first_name', 'middle_name', 'last_name', 'sr_code', 'age', 
      'sex', 'contact_number', 'present_address', 'email'
    ]
    widgets = {
      'profile_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'sr_code': forms.TextInput(attrs={'class': 'form-control'}),
      'age': forms.NumberInput(attrs={'class': 'form-control'}),
      'sex': forms.Select(choices=AlangilanUsers.SEX_CHOICES),
      'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
      'present_address': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'})
    }

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['email'].required = True

class StudentAppointment1Form(forms.ModelForm):
  class Meta:
    model = UserAppointment
    fields = [
      'course', 'department'
    ]
    widgets = {
      'course': forms.TextInput(attrs={'class': 'form-control'}),
      'department': forms.TextInput(attrs={'class': 'form-control'})
    }

class StudentAppointment2Form(forms.ModelForm):
  class Meta:
    model = UserAppointment
    fields = [
      'appointment_date', 'appointment_time'
    ]
    widgets = {
      'appointment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
      'appointment_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'})
    }