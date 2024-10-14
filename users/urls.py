from django.urls import path
from django.contrib import admin
from . import views

app_name = "users"

urlpatterns = [
  path("admin/", admin.site.urls),

  path("register/admin", views.admin_registration, name="admin_registration"),
  path("register/student", views.student_registration, name="student_registration"),

  path("bsu-alangilan/login", views.user_login, name="user_login"),
  path("bsu-alangilan/logout", views.user_logout, name="user_logout"),

  path("user-admin/dashboard", views.admin_dashboard, name="admin_dashboard"),
  path("user-admin/inventory", views.admin_inventory, name="admin_inventory"),
  path("user-admin/profile", views.admin_profile, name="admin_profile"),
  path("user-admin/student_app", views.admin_student_app, name="admin_student_app"),
  path("user-admin/student_history_profile", views.admin_student_history_profile, name="admin_student_history_profile"),
  path("user-admin/student_history", views.admin_student_history, name="admin_student_history"),
  path("user-admin/student_record_profile", views.admin_student_record_profile, name="admin_student_record_profile"),
  path("user-admin/student_records", views.admin_student_records, name="admin_student_records"),

  path("user-student/home", views.student_home, name="student_home"),
  path("user-student/appointment1", views.student_appointment1, name="student_appointment1"),
  path("user-student/appointment2", views.student_appointment2, name="student_appointment2"),
  path("user-student/appointment3", views.student_appointment3, name="student_appointment3"),
  path("user-student/appointment4_form1", views.student_appointment4_form1, name="student_appointment4_form1"),
  path("user-student/appointment4_form2", views.student_appointment4_form2, name="student_appointment4_form2"),
  path("user-student/appointment5", views.student_appointment5, name="student_appointment5"),
]
