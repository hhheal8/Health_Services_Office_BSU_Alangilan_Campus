from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
  path("register/admin/username", views.admin_registration, name="admin_registration"),
  path("login/", views.user_login, name="user_login"),
  path("admin/dashboard", views.admin_dashboard, name="admin_dashboard"),
  path("admin/inventory", views.admin_inventory, name="admin_inventory"),
  path("admin/profile", views.admin_profile, name="admin_profile"),
  path("admin/student_app", views.admin_student_app, name="admin_student_app"),
  path("admin/student_history_profile", views.admin_student_history_profile, name="admin_student_history_profile"),
  path("admin/student_history", views.admin_student_history, name="admin_student_history"),
  path("admin/student_record_profile", views.admin_student_record_profile, name="admin_student_record_profile"),
  path("admin/student_records", views.admin_student_records, name="admin_student_records")
]
