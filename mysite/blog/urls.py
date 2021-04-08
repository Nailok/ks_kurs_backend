from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, UserViewSet, DataTableViewSet
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter(trailing_slash=True)
router.register(r'client', ClientViewSet, base_name='')
router.register(r'user', UserViewSet, base_name='')
router.register(r'data', DataTableViewSet, base_name='')
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/token/', obtain_jwt_token)
]
