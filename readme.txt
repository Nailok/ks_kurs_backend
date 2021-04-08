mkdir djangoweb
cd djangoweb
python -m venv .env
.env\Scripts\activate
(.env) C:\my\project\web>
python -m pip install --upgrade pip

������� ���� requirements.txt

(.env) C:\my\project\web>pip install -r requirements.txt

(.env) C:\my\project\web>django-admin.exe startproject mysite
������ ��������� � settings.py


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mysite',
        'USER': 'mysite',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

������������� postgresql

psql -U postgres

������� ����� ����

CREATE DATABASE "mysite";
CREATE USER mysite WITH PASSWORD '12345678';
GRANT ALL PRIVILEGES ON DATABASE "mysite" to mysite;
\q


(.env) C:\my\project\web>cd mysite
(.env) C:\my\project\web\mysite>python manage.py migrate


(.env) C:\my\project\web\mysite>python manage.py startapp blog



(.env) C:\my\project\web\mysite>cd blog

� ���� models.py ���������

from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=10, null=True, verbose_name='���')
    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name="���� ����������")


� settings.py ��������� ��������� ����������

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'blog'
]

������� �������
(.env) C:\my\project\web\mysite>python manage.py makemigrations 

������� views

from rest_framework.permissions import AllowAny
from rest_framework import serializers, viewsets
from .models import Client


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('name', 'updated', )


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ClientSerializer

    def get_queryset(self):
        queryset = Client.objects.filter()
        return queryset

������� urls

from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet

router = DefaultRouter(trailing_slash=True)
router.register(r'client', ClientViewSet, base_name='')
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls))
]


� settings ������������� 
ROOT_URLCONF = 'blog.urls'


��������� ������ ����� curl















