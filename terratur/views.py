from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login as inicio_sesion
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages

def template_dashboard(request):
    return render(request, 'template_dashboard.html',{
    })

def dashboard(request):
    return render(request, 'dashboard.html',{
    })

def panel(request):
    return render(request, 'panel.html',{
    })

def login(request):
    return render(request, 'login.html',{
    })

def asesores(request):
    return render(request, 'asesores.html',{
    })

def comisiones(request):
    return render(request, 'comisiones.html',{
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            inicio_sesion(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('panel')
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html',{

    })


def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login')

