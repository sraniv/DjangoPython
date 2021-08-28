from django.urls import path, include
from . import views 
  
urlpatterns = [ 
    path('', views.index),
    path('auth_rest/',include('app_auth_rest.urls')),
    path('file_rest/',include('app_file_rest.urls')),
] 
