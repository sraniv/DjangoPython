from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Tinitiate Django Home Page from the APP: app_home !!")
