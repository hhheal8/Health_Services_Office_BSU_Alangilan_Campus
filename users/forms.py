from django import forms
from django.forms.widgets import PasswordInput
from .models import AlangilanUsers

class AdminRegistrationForm(forms.ModelForm):
  password = forms.CharField(widget=PasswordInput)
    
  class Meta:
    model = AlangilanUsers
    fields = [
      'username', 'first_name', 'last_name', 'middle_name', 'suffix', 
      'age', 'position', 'sex', 'contact_number', 'telephone_number', 
      'email', 'profile_image', 'present_address', 'home_address'       
    ]
        
  def save(self, commit=True):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password'])
    user.role = 'admin'
    user.is_staff = True  # Allows access to Django admin
    if commit:
      user.save()
    return user

class StudentRegistrationForm(forms.ModelForm):
  password = forms.CharField(widget=PasswordInput)
    
  class Meta:
    model = AlangilanUsers
    fields = [
      'username', 'first_name', 'last_name', 'middle_name', 'suffix', 
      'birth_date', 'sr_code', 'age', 'sex', 'contact_number', 
      'telephone_number', 'email', 'civil_status', 'gsuite', 'present_address', 
      'home_address', 'profile_image'
    ]
        
  def save(self, commit=True):
    user = super().save(commit=False)
    user.set_password(self.cleaned_data['password'])
    user.role = 'student'
    user.is_staff = False
    if commit:
      user.save()
    return user
