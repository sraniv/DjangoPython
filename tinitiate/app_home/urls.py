from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    # For URL: localhost:8000/ and view function: home
    # Usage Example URL: localhost:8000
    path('', views.home, name='home'),
]