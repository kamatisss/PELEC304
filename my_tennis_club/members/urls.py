
from django.urls import path
from . import views

urlpatterns = [
    path('member/', views.member, name='member'),
    path('members/', views.members, name='members'),
]
