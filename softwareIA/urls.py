from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/',include('softwareIA.aplicaciones.baseSistema.urls')),
    path('api/v1.0/compColorBack/',include('softwareIA.aplicaciones.colorBack.urls')),
    path('api/v1.0/usersManage/',include('softwareIA.aplicaciones.rest_auth.urls')),
    path('api/v1.0/usersManage/register',include('softwareIA.aplicaciones.rest_auth.registration.urls')),
]
