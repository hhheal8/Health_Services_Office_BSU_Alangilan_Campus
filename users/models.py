from django.db import models
from django.contrib.auth.models import AbstractUser

class AlangilanUsers(AbstractUser):

  ROLE_CHOICES = (
    ("admin", "Admin"),
    ("student", "Student")
  )

  POSITION_CHOICES = [
    ("doctor", "Doctor"),
    ("nurse", "Nurse"),
  ]

  SEX_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
  ]
  
  role = models.CharField(max_length=10, choices=ROLE_CHOICES)
  middle_name = models.CharField(max_length=50, blank=True, null=True)
  suffix = models.CharField(max_length=10, blank=True, null=True)
  birth_date = models.DateField(null=True, blank=True)
  sr_code = models.CharField(max_length=50)
  age = models.IntegerField(blank=False, null=False)
  position = models.CharField(max_length=6, choices=POSITION_CHOICES)
  sex = models.CharField(max_length=6, choices=SEX_CHOICES)
  contact_number = models.CharField(max_length=15)
  telephone_number = models.CharField(max_length=15)
  civil_status = models.CharField(max_length=20)
  gsuite = models.CharField(max_length=50)
  present_address = models.CharField(max_length=255)
  home_address = models.CharField(max_length=255)
  profile_image = models.ImageField(upload_to="profile_images/")

  def __str__(self):
    return self.username