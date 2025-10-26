from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


def members(request):
   return render(request, 'myfirst.html')


def member(request):
    return HttpResponse("Malalakas na tao si barry sa free fire")


# Create your views here.
