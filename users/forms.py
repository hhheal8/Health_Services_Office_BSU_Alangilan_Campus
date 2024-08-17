from django import forms
from . import models

class CreateUsers(forms.ModelForm):
  class Meta:
    model = models.Users
    fields = [
      'last_name', 'first_name', 'middle_name'
    ]

  
