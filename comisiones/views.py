from django.shortcuts import render, redirect, get_object_or_404
from terratur_app.models import Comision
from .forms import ComisionesForm, ComisionesEditarForm

def listar_comisiones(request):
    comisiones = Comision.objects.all()
    return render(request, 'comisiones.html', {"comisiones": comisiones})

def registro_comision(request):
    if request.method == 'GET':
        return render(request, 'registro_comision.html', {"form": ComisionesForm})
    else:
        form = ComisionesForm(request.POST)
        if form.is_valid():
            nueva_comision = form.save(commit=False)
            nueva_comision.save()
        return redirect('comisiones')

def edicion_comision(request, id):

    comision = get_object_or_404(Comision, id=id)

    data = {
        'form': ComisionesEditarForm(instance=comision)
    }

    if request.method == 'POST':
        formulario = ComisionesEditarForm(data=request.POST, instance=comision, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="comisiones")
        data["form"] = formulario    

    return render(request, "edicion_comision.html", data)


