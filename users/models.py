from django.db import models
from django.contrib.auth.models import AbstractUser

class UserAdmin(AbstractUser):

  groups = models.ManyToManyField(
    "auth.Group",
    related_name="user_admin_group",
    blank=True,
    help_text=("The groups this user belongs to."),
    verbose_name=("groups"),
  )

  user_permissions = models.ManyToManyField(
    "auth.Permission",
    related_name="user_admin_permissions",
    blank=True,
    help_text=("Specific permissions for this` user."),
    verbose_name=("user permissions"),
  )

  POSITION_CHOICES = [
    ("doctor", "Doctor"),
    ("nurse", "Nurse"),
  ]

  SEX_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
  ]

  middle_name = models.CharField(max_length=50, blank=True, null=True)
  suffix = models.CharField(max_length=10, blank=True, null=True)
  age = models.IntegerField(blank=False, null=False)
  position = models.CharField(max_length=6, choices=POSITION_CHOICES)
  sex = models.CharField(max_length=6, choices=SEX_CHOICES)
  contact_number = models.CharField(max_length=15)
  telephone_number = models.CharField(max_length=15, blank=True, null=True)
  profile_image = models.ImageField(upload_to="profile_images/")
  present_address = models.CharField(max_length=255)
  home_address = models.CharField(max_length=255)

class UserStudent(AbstractUser):

  groups = models.ManyToManyField(
    "auth.Group",
    related_name="user_student_group",  # Unique related_name
    blank=True,
    help_text=("The groups this user belongs to."),
    verbose_name=("groups"),
  )

  user_permissions = models.ManyToManyField(
    "auth.Permission",
    related_name="user_student_permissions",  # Unique related_name
    blank=True,
    help_text=("Specific permissions for this user."),
    verbose_name=("user permissions"),
  )

  SEX_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
  ]

  middle_name = models.CharField(max_length=50, blank=True, null=True)
  suffix = models.CharField(max_length=10, blank=True, null=True)
  birth_date = models.DateField(null=True, blank=True)
  sr_code = models.CharField(max_length=50)
  age = models.IntegerField(blank=False, null=False)
  sex = models.CharField(max_length=6, choices=SEX_CHOICES)
  contact_number = models.CharField(max_length=15)
  telephone_number = models.CharField(max_length=15)
  civil_status = models.CharField(max_length=20)
  gsuite = models.CharField(max_length=50)
  present_address = models.CharField(max_length=255)
  home_address = models.CharField(max_length=255)
  profile_image = models.ImageField(upload_to="profile_images/")