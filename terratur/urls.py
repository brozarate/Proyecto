"""
terratur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cgitb import html
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.panel, name='panel'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('template/', views.template_dashboard, name='template_dashboard'),
    path('asesores/', include('terratur_app.urls')), #esta ruta esta asociada a la ruta urls creada en la carpeta terratur_app
    path('comisiones/', include('comisiones.urls')),
    #path('comisiones/', views.comisiones, name='comisiones'),
    # path('listar_comisiones/', views.listar_comisiones, name='listar_comisiones'),
    # path('registro_comision/', views.registro_comision, name='registro_comision'),
    # path('edicion_comision/', views.edicion_comision, name='edicion_comision/'),

]
