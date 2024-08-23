from django import forms
from .models import UserAdmin

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

  
