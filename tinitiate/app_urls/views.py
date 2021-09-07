from django.shortcuts import render
from django.http import HttpResponse

def message(request):
    return HttpResponse("Welcome to Tinitiate Django message page")

def year_month(request, in_year, in_month):
    response = "Input Year: " + str(in_year) + " Input Month: " + str(in_month)
    return HttpResponse(response)

def slug_test(request, in_slug):
    response = "Input Slug: " + in_slug
    return HttpResponse(response)
