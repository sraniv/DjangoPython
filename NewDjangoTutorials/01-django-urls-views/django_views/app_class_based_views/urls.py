from django.urls import path
from . import views

urlpatterns = [

    # localhost:8000/app_class_based_views/data/
    path('data/', views.DataView.as_view(), name='data'),
]