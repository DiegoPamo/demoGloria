from django.shortcuts import render, redirect
from .forms import NewUserForm, NewControl_NetoForm
from django.contrib.auth import login, authenticate, logout as django_logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    form = NewControl_NetoForm()
    return render(request, 'chart-flot.html', context={'form_control': form})

# registro de usuario


def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Usuario creado con exito")
            return redirect('index')
        messages.error(request, "Error al momento de crear usuario")
    form = NewUserForm()
    return render(request, "autentificacion/register.html", context={'form_user': form})


# Funcion para el logueo de usuario
def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(
                    request, f"Te logueaste con el usuario {username}.")
                return redirect('index')
            else:
                messages.error(
                    request, "Error al introducir credenciales de logueo")
        else:
            messages.error(
                request, "Error al introducir credenciales de logueo")
    form = AuthenticationForm()
    return render(request, 'autentificacion/login.html', context={'login_form': form})

# funcion de logout


def logout(request):
    django_logout(request)
    messages.info(request, "Usuario delogueado")
    return redirect('login')
