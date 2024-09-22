from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import UserAdmin, UserStudent

class UserAdminBackend(BaseBackend):
  def authenticate(self, request, username=None, password=None, **kwargs):
    try:
      user = UserAdmin.objects.get(username=username)
      if user.check_password(password):
        return user
    except UserAdmin.DoesNotExist:
      return None

  def get_user(self, user_id):
    try:
      return UserAdmin.objects.get(pk=user_id)
    except UserAdmin.DoesNotExist:
      return None

class UserStudentBackend(BaseBackend):
  def authenticate(self, request, username=None, password=None, **kwargs):
    try:
      user = UserStudent.objects.get(username=username)
      if user.check_password(password):
        return user
    except UserStudent.DoesNotExist:
      return None

  def get_user(self, user_id):
    try:
      return UserStudent.objects.get(pk=user_id)
    except UserStudent.DoesNotExist:
      return None
