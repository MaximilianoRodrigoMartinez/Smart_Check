from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Local, Empleado, Horario
from .forms import HorarioForm, EmpleadoForm, LocalForm
from django.contrib.auth.decorators import permission_required, login_required, user_passes_test
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout



# Create your views here.

def es_rrhh(user):
    return user.username == 'RRHH'

def es_del_grupo_locales(user):
    return user.groups.filter(name='Locales').exists()

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Inicio')  
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

def inicio(req):

    return render(req, "index.html", {})


@user_passes_test(es_rrhh)
def crea_local(req):
    if req.method == 'POST':
        form = LocalForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista_locales') 
    else:
        form = LocalForm()
    return render(req, 'crea_local.html', {'form': form})

@user_passes_test(es_rrhh)
def lista_locales(req):

    lista_locales = Local.objects.prefetch_related('empleado_set').all()

    return render(req, 'lista_locales.html', {'lista_locales': lista_locales})

@user_passes_test(es_rrhh)
def crea_empleado(req):
    if req.method == 'POST':
        form = EmpleadoForm(req.POST, req.FILES)  
        if form.is_valid():
            form.save()
            return redirect('Lista_empleados')
    else:
        form = EmpleadoForm()
    return render(req, 'crea_empleado.html', {'form': form})



@user_passes_test(es_rrhh)
def lista_empleados(req):

    empleados = Empleado.objects.all()  

    return render(req, "lista_empleados.html", {"empleados": empleados})


@user_passes_test(es_rrhh)
def asigna_horarios(req):
    if req.method == 'POST':
        form = HorarioForm(req.POST)
        if form.is_valid():
            horario = form.save(commit=False)  
            local_id = req.POST.get('local_id')  
            horario.local_id = local_id  
            horario.save()  
            return redirect('Lista_horarios')
    else:
        form = HorarioForm()

    return render(req, 'asigna_horarios.html', {'form': form, 'lista_locales': Local.objects.all()})


@user_passes_test(es_rrhh)
def lista_horarios(req):

    lista = Horario.objects.all()

    return render(req, "lista_horarios.html", {"lista_horarios": lista})

def logout_view(request):
    auth_logout(request)
    return redirect('login_view')
                    











