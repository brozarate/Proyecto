from django.contrib import admin
# Register your models here.
from .models import GerenteDeCuenta, Asesor, Comision


class AsesorAdmin(admin.ModelAdmin):
    search_fields = ('first_name'),
    ordering = ['first_name']

class ComisionAdmin(admin.ModelAdmin):
    ordering = ['Asesor']
    autocomplete_fields = ['Asesor']   


admin.site.register(GerenteDeCuenta)
admin.site.register(Asesor, AsesorAdmin)
admin.site.register(Comision, ComisionAdmin)

