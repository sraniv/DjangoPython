from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('app_urls_views/', include('app_urls_views.urls')),
    path('app_multiple_views/', include('app_multiple_views.urls')),
    path('app_class_based_views/', include('app_class_based_views.urls')),
    path('app_view_return_types/', include('app_view_return_types.urls')),
    path('admin/', admin.site.urls),
]
