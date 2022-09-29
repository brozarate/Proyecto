from django import forms
from django.forms import ModelForm
#from .models import Comision
from terratur_app.models import Comision


class ComisionesForm(forms.ModelForm):
    class Meta:
        model = Comision
        #fields = ['Asesor', 'destino', 'total_sale', 'advisory_commission', 'commission_to_pay', 'commission_status']
        fields = '__all__'
        widgets = {
            'Asesor': forms.Select(attrs={'class': 'form-select mb-2', 'readonly':'readonly'}),
            'destino': forms.Select(attrs={'class': 'form-select mb-2'}),
            'total_sale': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Ingresa el valor de venta' }),
            'advisory_commission': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'commission_to_pay': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'commission_status': forms.Select(attrs={'class': 'form-select mb-2'}),
            #'estado_comision' : forms.Select(attrs={'class': 'form-select mb-2'}),
        }


class ComisionesEditarForm(forms.ModelForm):
    class Meta:
        model = Comision
        fields = ['Asesor', 'destino', 'total_sale', 'advisory_commission', 'commission_to_pay', 'commission_status']
        #fields = '__all__'
        widgets = {
            'Asesor': forms.Select(attrs={'class': 'form-select mb-2', 'readonly':'readonly'}),
            'destino': forms.Select(attrs={'class': 'form-select mb-2'}),
            'total_sale': forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Ingresa el valor de venta' }),
            'advisory_commission': forms.TextInput(attrs={'class': 'form-control mb-2', 'readonly':'readonly'}),
            'commission_to_pay': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'commission_status': forms.Select(attrs={'class': 'form-select mb-2'}),
            #'estado_comision' : forms.Select(attrs={'class': 'form-select mb-2'}),
        }