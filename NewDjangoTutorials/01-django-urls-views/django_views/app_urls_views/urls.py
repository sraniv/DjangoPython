from django.urls import path, re_path
from . import views

urlpatterns = [

    # Simple URL
    # localhost:8000/app_urls_views/view_no_param
    # ###############################################################################
    path('view_no_param/', views.view_no_param, name='view_no_param'),

    # Patterns
    # localhost:8000/app_urls_views/data/1234
    # localhost:8000/app_urls_views/data/abcd
    # ###############################################################################
    re_path(r'^data/(?P<data>[0-9]{4})$', views.view_numbers),
    re_path(r'^data/(?P<data>[-\w]+)$', views.view_strings),

    # Passing Parameters to Views
    # localhost:8000/app_urls_views/view_integer_param/1
    # localhost:8000/app_urls_views/view_string_param/Hello
    # localhost:8000/app_urls_views/even_or_odd/1
    # ###############################################################################   
    path('view_integer_param/<int:in_data>', views.view_integer_param, name='view_integer_param'),
    path('view_string_param/<str:in_data>', views.view_string_param, name='view_string_param'),
    path('even_or_odd/<int:in_number>', views.even_or_odd, name='even_or_odd'),

]