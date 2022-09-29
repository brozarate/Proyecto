from django.shortcuts import render, redirect
from .models import Asesor

# Create your views here.

def listar_asesores(request):
    asesores = Asesor.objects.all()
    return render(request, 'asesores.html', {"asesores": asesores})

def crear_asesor(request):
    asesor = Asesor(first_name=request.POST['first_name'], last_name=request.POST['last_name'], phone=request.POST['phone'], email=request.POST['email'], advisory_status=request.POST['advisory_status'])
    asesor.save()
    return redirect('/asesores/')

def delete_asesor(request, id):
    asesor = Asesor.objects.get(id=id)
    asesor.delete()
    return redirect('/asesores/')


def edicion_asesor(request, id):
    asesor = Asesor.objects.get(id=id)
    return render(request, 'edicion_asesor.html', {"asesor":asesor})

def editar_asesor(request, id):
    id = int(request.POST['id'])
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    phone=request.POST['phone']
    email=request.POST['email']
    #commission=request.POST['commission']
    advisory_status=request.POST['advisory_status']

    asesor = Asesor.objects.get(id=id)
    asesor.first_name = first_name
    asesor.last_name = last_name
    asesor.phone = phone
    asesor.email = email
    #asesor.commission = commission
    asesor.advisory_status = advisory_status
    asesor.save()
    return redirect('/asesores/')
