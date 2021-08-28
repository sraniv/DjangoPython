from django.shortcuts import render
"""
* Open a browser to test the URLs defined so far
 *  http://127.0.0.1:8000/app_views/view_no_param
 *  http://127.0.0.1:8000/app_views/view_integer_param/1
 *  http://127.0.0.1:8000/app_views/view_string_param/hello
 *  http://127.0.0.1:8000/app_views/even_or_odd/4
 *  http://127.0.0.1:8000/app_views/even_or_odd/5
 """
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def view_no_param(request):
    return HttpResponse("Welcome to Tinitiate Django Test Home Page Version 1.0")


def view_integer_param(request, in_data):
    response = "Integer Data Provided: " + str(in_data)
    return HttpResponse(response)


def view_string_param(request, in_data):
    response = "String Data Provided: " + in_data
    return HttpResponse(response)


def even_or_odd(request, in_number):
    s_data = str(in_number)

    if (in_number % 2) == 0:
        response = s_data + " is a even number"
    else:
        response = s_data + " is a odd number"

    return HttpResponse(response)