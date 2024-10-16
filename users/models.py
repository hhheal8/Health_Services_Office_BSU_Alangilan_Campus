from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class AlangilanUsers(AbstractUser):

  ROLE_CHOICES = (
    ("admin", "Admin"),
    ("student", "Student")
  )
  role = models.CharField(max_length=10, choices=ROLE_CHOICES)

  POSITION_CHOICES = [
    ("doctor", "Doctor"),
    ("nurse", "Nurse"),
  ]
  position = models.CharField(max_length=6, choices=POSITION_CHOICES)

  SEX_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
  ]
  sex = models.CharField(max_length=6, choices=SEX_CHOICES)
  
  middle_name = models.CharField(max_length=50, blank=True, null=True)
  suffix = models.CharField(max_length=10, blank=True, null=True)
  birth_date = models.DateField(null=True, blank=True)
  sr_code = models.CharField(max_length=50)
  age = models.IntegerField(blank=False, null=False)
  contact_number = models.CharField(max_length=15)
  telephone_number = models.CharField(max_length=15)
  civil_status = models.CharField(max_length=20)
  gsuite = models.CharField(max_length=50)
  present_address = models.CharField(max_length=255)
  home_address = models.CharField(max_length=255)
  profile_image = models.ImageField(upload_to="profile_images/")

  @property
  def full_name(self):
    return f"{self.first_name} {self.middle_name or ''} {self.last_name}"
  
  def __str__(self):
    return self.username

class UserAppointment(models.Model):

  user = models.ForeignKey(AlangilanUsers, on_delete=models.CASCADE)
  
  course = models.CharField(max_length=100)
  department = models.CharField(max_length=100)

  def __str__(self):
    return f"Appointment for {self.user.full_name}"
