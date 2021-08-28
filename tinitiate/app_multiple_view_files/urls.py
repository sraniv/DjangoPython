from django.conf.urls import url
from django.urls import path
from .views import greetings
from .views import calc

""" STEP 6. Run Project and Test URLS in Browser
* At commandline start the project, using the command:
```
"""
"""
C:\sers\rvish\sudha\DjangoPython\tinitiate>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
August 27, 2021 - 11:44:39
Django version 3.2.6, using settings 'tinitiate.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.


```
* Open a browser to test the URLs defined so far
 * http://127.0.0.1:8000/multiple_views/num_square/2
 * http://127.0.0.1:8000/multiple_views/num_square/4
 * http://127.0.0.1:8000/multiple_views/hello/tinitiate
 * http://127.0.0.1:8000/multiple_views/bday/tinitiate
"""

urlpatterns = [
    # For URL: localhost:8000/multiple_views/hello and view function: hello
    # Usage Example URL: localhost:8000/multiple_views/hello/tinitiate
    path('hello/<str:in_data>', greetings.hello, name='hello'),

    # For URL: localhost:8000/multiple_views/bday and view function: bday
    # Usage Example URL: localhost:8000/multiple_views/bday/tinitiate
    path('bday/<str:in_data>', greetings.bday, name='bday'),

    # For URL: localhost:8000/multiple_views/num_square and view function: num_square
    # Usage Example URL: localhost:8000/multiple_views/num_square/3
    path('num_square/<int:in_number>', calc.num_square, name='num_square'),

    # For URL: localhost:8000/multiple_views/even_or_odd and view function: even_or_odd
    # Usage Example URL: localhost:8000/multiple_views/even_or_odd/1
    path('even_or_odd/<int:in_number>', calc.even_or_odd, name='even_or_odd'),
]