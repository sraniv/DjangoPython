from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def app_home(request):
    return HttpResponse("Welcome to Tinitiate Django app_ti Home Page")