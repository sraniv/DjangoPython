from django.urls import path
from . import views

"""
```
python manage.py runserver
```
* Open a browser to test the URLs defined so far
 *  http://127.0.0.1:8000/app_django_html_templates/st_java
 *  http://127.0.0.1:8000/app_django_html_templates/st_python
"""

urlpatterns = [
    # For URL: localhost:8000
    path('st_python/', views.simple_template_python, name='simple_template_python'),
    path('st_java/', views.simple_template_java, name='simple_template_java'),
]