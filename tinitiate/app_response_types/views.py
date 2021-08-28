from email.mime import image
from io import BytesIO
from tkinter import Image

from django.shortcuts import render

"""
 Here we create a `views.py` file with various methods demonstrating 
  various Response Types.
* Here we demonstrate 
  * View Returning plain text 
  * View Returning xml text
  * View Returning html (Rich Text) 
  * View Returning json
  * View Streaming HTTP Response
"""

# Create your views here.
from django.http import HttpResponse, FileResponse, JsonResponse, StreamingHttpResponse
import csv
import requests
#from PIL import Image
#from io import BytesIO

def http_response_plain_text(request):
    return HttpResponse("Plain Text Response", content_type="text/plain")

def http_response_xml_text(request):
    response = """<?xml version="1.0" encoding="UTF-8"?>
                  <data>
                      <topic>Python Django</topic>
                      <heading>Response Types</heading>
                  </data>"""

    return HttpResponse(response, content_type="text/xml")

def http_response_html(request):

    html_text = """<h1>HTML Response </h1>
                <p style="background-color:red; color:white;">HTML Response Output</p>"""

    return HttpResponse(html_text)

def json_response(request):
    return JsonResponse({'data':'tinitiate'})


def file_response(request):

    """
    _file = 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png'
    response = requests.get(_file)
    img = Image.open(BytesIO(response.content))
    response = FileResponse(img)
    response['Content-Disposition'] = "attachment; filename=%s" % image.svg
    return response
    """
    _file = "C:\\Users\\rvish\\sudha\\DjangoPython\\tinitiate\\images\\pythonlogo.png"
    img = open(_file, 'rb')
    response = FileResponse(img)

    return response

######################################################################
## STREAMING EXAMPLE
## This will download a file with 1 to 100 each number on a new line
######################################################################
def generator():
    for x in range(100):
        yield str(x) + "\n"

def streaming_http_response(queryset):
    response = StreamingHttpResponse( streaming_content=generator(),content_type='text/plain')

    response['Content-Disposition'] = 'attachment;filename=data.txt'
    return response