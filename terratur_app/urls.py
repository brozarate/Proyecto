from django.urls import path
from .views import listar_asesores, crear_asesor, delete_asesor, edicion_asesor, editar_asesor #listar_comisiones, registro_comision, edicion_comision

urlpatterns = [
    path('', listar_asesores, name='asesores'),
    path('nuevo_asesor/', crear_asesor, name='nuevo_asesor'),
    path('delete_asesor/<id>', delete_asesor),
    path('edicion_asesor/<id>', edicion_asesor),
    path('editar_asesor/<id>', editar_asesor),
    # path('comisiones/', listar_comisiones, name='comisiones'),
    # path('registro_comision/', registro_comision, name='registro_comision'),
    # path('edicion_comision/<id>', edicion_comision),
]

