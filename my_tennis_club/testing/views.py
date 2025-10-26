from django.shortcuts import render
from django.http import HttpResponse

def student_profile(request):
    student = [
        {"name":"Harry", "age":21},
        {"name":"Hans", "age":20},
    ]
    return render(request,'student_profile.html',{"student":student})

# Create your views here.
