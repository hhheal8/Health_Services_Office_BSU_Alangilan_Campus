from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class AlangilanUsers(AbstractUser):

  ROLE_CHOICES = (
    ("admin", "Admin"),
    ("student", "Student")
  )
  role = models.CharField(max_length=10, choices=ROLE_CHOICES, null=False, blank=False)

  POSITION_CHOICES = [
    ("doctor", "Doctor"),
    ("nurse", "Nurse"),
  ]
  position = models.CharField(max_length=6, choices=POSITION_CHOICES, null=False, blank=False)

  SEX_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
  ]
  sex = models.CharField(max_length=6, choices=SEX_CHOICES, null=True, blank=True)
  
  middle_name = models.CharField(max_length=50, null=True, blank=True)
  suffix = models.CharField(max_length=10, null=True, blank=True)
  birth_date = models.DateField()
  sr_code = models.CharField(max_length=50, null=False, blank=False)
  age = models.IntegerField(null=False, blank=False)
  contact_number = models.CharField(max_length=15, null=True, blank=True)
  telephone_number = models.CharField(max_length=15, null=True, blank=True)
  civil_status = models.CharField(max_length=20, null=True, blank=True)
  gsuite = models.CharField(max_length=50, null=True, blank=True)
  present_address = models.CharField(max_length=255, null=True, blank=True)
  home_address = models.CharField(max_length=255, null=True, blank=True)
  profile_image = models.ImageField(upload_to="profile_images/", null=True, blank=True)

  @property
  def full_name(self):
    return f"{self.first_name} {self.middle_name or ''} {self.last_name}"
  
  def __str__(self):
    return self.username

class UserAppointment(models.Model):

  user = models.ForeignKey(AlangilanUsers, on_delete=models.CASCADE)

  course = models.CharField(max_length=100, null=False, blank=False)
  department = models.CharField(max_length=100, null=False, blank=False)
  appointment_date = models.DateField(null=True, blank=True)
  appointment_time = models.TimeField(null=True, blank=True)

  def __str__(self):
    return f"Appointment for {self.user.full_name}"
