from django.db import models

class Users(models.Model):
  username = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  first_name = models.CharField(max_length=50)
  middle_name = models.CharField(max_length=50)

  def __str__(self):
    return self.first_name