from django.urls import path
from . import views

#C:\sers\rvish\sudha\DjangoPython\tinitiate>python manage.py runserver
# http://127.0.0.1:8000/app_ti


urlpatterns = [
    # For URL: localhost:8000 and view function: app_home
    path('', views.app_home, name='app_home'),
]