from django.shortcuts import render
# http://127.0.0.1:8000/app_ti
# Create your views here.
from django.http import HttpResponse

def app_home(request):
    return HttpResponse("Welcome to Tinitiate Django app_ti Home Page")