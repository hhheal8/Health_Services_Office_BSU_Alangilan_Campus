from django import forms
from .models import UserAdmin, UserStudent

class UserAdminRegistration(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)

  class Meta:
    model = UserAdmin
    
    fields = [
      "username", "password", "first_name", "last_name", "middle_name", 
      "suffix", "age", "position", "sex", "contact_number", 
      "telephone_number", "profile_image", "present_address", "home_address"
    ]

    widgets = {
      "position": forms.Select(choices=UserAdmin.POSITION_CHOICES),
      "sex": forms.Select(choices=UserAdmin.SEX_CHOICES)
    }

class UserStudentRegistration(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput)

  class Meta:
    model = UserStudent

    fields = [
      "middle_name", "suffix", "birth_date", "sr_code", "age", 
      "sex", "contact_number", "telephone_number", "civil_status", "gsuite", 
      "present_address", "home_address", "profile_image"
    ]

    widgets = {
      "sex": forms.Select(choices=UserStudent.SEX_CHOICES),
      "birth_date": forms.DateInput(attrs={"type": "date"})
    }

