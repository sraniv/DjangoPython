from django.urls import path
from . import views

urlpatterns = [
    # For URL: localhost:8000 and view function: app_home
    path('', views.app_home, name='app_home'),
]