"""django_drf_project URL Configuration"""
from django.contrib import admin
from django.urls import path, include

from profile_api.routers import urlpatterns as profile_api_urls


api_urls = profile_api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_urls)),
]
