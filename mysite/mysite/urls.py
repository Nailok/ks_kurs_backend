from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('admin/', admin.site.urls),
]
