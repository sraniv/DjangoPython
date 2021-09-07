from django.conf.urls import include, url
from django.urls import path, re_path

from . import views

# import app_views #import urls as app_views_urls

"""
* **TESTING**
>python manage.py runserver
* Open a browser to test the URLs defined so far
  * For Home Page Use: `http://127.0.0.1:8000/app_urls/message/`
  * For Regular Expressions parameters Page Use: `http://127.0.0.1:8000/app_urls/year_month/2002/11/`
  * For Include URLs from other apps Use: `http://127.0.0.1:8000/app_urls/include_test/view_no_param/`

"""

urlpatterns = [
    # Path
    path('message/', views.message, name='message'),
    path('slug_test/<slug:in_slug>/', views.slug_test),

    # RegEx Path
    re_path(r'^year_month/(?P<in_year>[0-9]{4})/(?P<in_month>[0-9]{2})/$', views.year_month),

    # Include
    url('include_test/', include('app_views.urls')),
]