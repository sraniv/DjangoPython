from django.urls import path
from . import views

"""
```
python manage.py runserver
```
* Open a browser to test the URLs defined so far
*  http://127.0.0.1:8000/app_django_templates_inheritance/ti_blocks

"""

urlpatterns = [
    # For URL: localhost:8000
    path('ti_blocks', views.template_blocks, name='template_blocks'),
]