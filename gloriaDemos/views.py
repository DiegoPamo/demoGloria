from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

def index(request):
    return render(request, 'chart-flot.html')

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
    return render(request,"autentificacion/register.html",context={'form_user':form})