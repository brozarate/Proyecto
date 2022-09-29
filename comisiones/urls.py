from django.urls import path
from .views import listar_comisiones, registro_comision, edicion_comision

urlpatterns = [
    path('', listar_comisiones, name='comisiones'),
    path('registro_comision/', registro_comision, name='registro_comision'),
    path('edicion_comision/<id>', edicion_comision, name='edicion_comision'),
]