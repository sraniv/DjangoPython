from django.urls import path
from . import views

urlpatterns = [
    # For URL: localhost:8000/view_no_param and view function: view_no_param
    path('view_no_param/', views.view_no_param, name='view_no_param'),

    # For URL: localhost:8000/view_integer_param and view function: view_integer_param
    # Usage Example URL: localhost:8000/view_integer_param/1
    path('view_integer_param/<int:in_data>', views.view_integer_param, name='view_integer_param'),

    # For URL: localhost:8000/view_string_param and view function: view_string_param
    # Usage Example URL: localhost:8000/view_string_param/Hello
    path('view_string_param/<str:in_data>', views.view_string_param, name='view_string_param'),

    # For URL: localhost:8000/even_or_odd and view function: even_or_odd
    # Usage Example URL: localhost:8000/even_or_odd/1
    path('even_or_odd/<int:in_number>', views.even_or_odd, name='even_or_odd'),
]