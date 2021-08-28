from django.urls import path
from . import views

"""
Open a browser to test the URLs defined so far
  *  http://127.0.0.1:8000/app_response_types/plain_text
  *  http://127.0.0.1:8000/app_response_types/xml_text
  *  http://127.0.0.1:8000/app_response_types/json_response
  *  http://127.0.0.1:8000/app_response_types/html_response
  *  http://127.0.0.1:8000/app_response_types/streaming
  *  http://127.0.0.1:8000/app_response_types/file_response [Under Development]
"""

urlpatterns = [
    path('plain_text/', views.http_response_plain_text, name='http_response_plain_text'),
    path('xml_text/', views.http_response_xml_text, name='http_response_xml_text'),
    path('json_response/', views.json_response, name='json_response'),
    path('html_response/', views.http_response_html, name='http_response_html'),
    path('streaming/', views.streaming_http_response, name='streaming_http_response'),
    path('file_response/', views.file_response, name='file_response'),
]