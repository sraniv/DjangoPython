from django.urls import path
from . import views

urlpatterns = [
    path('random_number/', views.random_number, name='random_number'),
    path('even_odd/', views.even_odd, name='even_odd'),
    path('get_custom_header/', views.get_custom_header, name='get_custom_header'),
]
