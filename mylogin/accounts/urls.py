from django.urls import path
from . import views

urlpatterns = [
    path("enroll/", views.enroll_student, name="enroll_student"),
    path("success/", views.enroll_success,name="enroll_success"),
]