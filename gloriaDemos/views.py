from django.shortcuts import render, redirect
from .forms import NewUserForm, NewControl_NetoForm
from django.contrib.auth import login, authenticate, logout as django_logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Control_cont_neto
from django.urls import reverse

# DEPENDENCIAS PDF
import pdfkit
from django.http import HttpResponse
from django.template.loader import render_to_string

from xhtml2pdf import pisa
from django.template.loader import get_template
# config = pdfkit.configuration(wkhtmltopdf=r"C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")

def index(request):
    if request.method == 'POST':
        form = NewControl_NetoForm(request.POST)
        if form.is_valid():
            instancia = form.save(commit=False)
            
            campos = ['sub_grupo1', 'sub_grupo2', 'sub_grupo3', 'sub_grupo4', 'sub_grupo5',
              'promedio', 'rango', 'hora_reg', 'cilindro1', 'cilindro2', 'cilindro3']
            
            for campo in campos:
                valores = request.POST.getlist(campo + '[]')
                setattr(instancia, campo, valores)
      
            instancia.save()
            
            return redirect('tables')
    else:
        form = NewControl_NetoForm()
    return render(request, 'register_cont.html', context={'form_control':form})

def tables(request):
    registros = Control_cont_neto.objects.order_by('-fecha')

    for registro in registros:
        promedios = registro.promedio  # Obtener el array de promedios
        if promedios:
            # Convertir los valores a tipo float y calcular el promedio
            promedios_float = [float(valor) for valor in promedios]
            total_promedios = sum(promedios_float)
            promedio_final = round(total_promedios / len(promedios_float), 2)
            registro.promedio_final = promedio_final
            
            # Calcular el margen de error
            valor_esperado = 410
            diferencia_absoluta = abs(promedio_final - valor_esperado)
            margen_error = (diferencia_absoluta / valor_esperado) * 100
            registro.margen_error = round(margen_error, 2)
        else:
            registro.promedio_final = 0  # Opcional: si no hay valores, asignar un valor predeterminado
            registro.margen_error = 0  # Opcional: si no hay valores, asignar un margen de error de 0

    return render(request,'tables.html',{'registros': registros})

def edit_register(request,id):
    modelo = Control_cont_neto.objects.get(id=id)
    form = NewControl_NetoForm(instance=modelo)

    if request.method == 'POST':
        form = NewControl_NetoForm(request.POST, instance=modelo)
        if form.is_valid():
            instancia = form.save(commit=False)
            campos = ['sub_grupo1', 'sub_grupo2', 'sub_grupo3', 'sub_grupo4', 'sub_grupo5',
                      'promedio', 'rango', 'hora_reg', 'cilindro1', 'cilindro2', 'cilindro3']

            for campo in campos:
                valores = request.POST.getlist(campo + '[]')
                setattr(instancia, campo, valores)

            instancia.save()
            return redirect('edit_register', modelo.id)

    context = {
        'modelo': modelo,
        'form_control': form,
    }

    return render(request, 'register_cont.html', context)


def generar_pdf(request,id):
    modelo = Control_cont_neto.objects.get(id=id)

    cilindro1 = modelo.cilindro1
    cilindro1_groups = [cilindro1[i:i+2] for i in range(0, len(cilindro1), 2)]
    tr_count = 48 - len(cilindro1_groups)
    cilindro1_extended = ['-'] * tr_count

    cilindro2 = modelo.cilindro2
    cilindro2_groups = [cilindro2[i:i+2] for i in range(0, len(cilindro2), 2)]
    tr_count2 = 48 - len(cilindro2_groups)
    cilindro2_extended = ['-'] * tr_count2

    cilindro3 = modelo.cilindro3
    cilindro3_groups = [cilindro3[i:i+2] for i in range(0, len(cilindro3), 2)]
    tr_count3 = 48 - len(cilindro3_groups)
    cilindro3_extended = ['-'] * tr_count3

    context = {
        'data': modelo,
        'data2': {
            'cilindro1_groups': cilindro1_groups,
            'tr_count': tr_count,
            'cilindro1_extended': cilindro1_extended,
        },
        'data3': {
            'cilindro2_groups': cilindro2_groups,
            'tr_count2': tr_count2,
            'cilindro2_extended': cilindro2_extended,
        },
        'data4': {
            'cilindro3_groups': cilindro3_groups,
            'tr_count3': tr_count3,
            'cilindro3_extended': cilindro3_extended,
        },
    }

    # Renderiza el HTML con los datos
    html = render_to_string('pdfs/gloriaPDF.html', context=context)

    # Crea un objeto HttpResponse con las cabeceras PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mi_pdf.pdf"'

    # Genera el PDF utilizando xhtml2pdf
    pisa_status = pisa.CreatePDF(html, dest=response)

    # Verifica si hubo errores al generar el PDF
    if pisa_status.err:
        return HttpResponse('Hubo errores al generar el PDF')

    return response


###########################
########USUARIO VIEWS#######
############################

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


# Funcion para el logueo de usuario
def login_user(request):
    if request.method == "POST":
        form  = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Te logueaste con el usuario {username}.")
                return redirect('index')
            else:
                messages.error(request, "Error al introducir credenciales de logueo")
        else:
            messages.error(request, "Error al introducir credenciales de logueo")
    form = AuthenticationForm()
    return render(request,'autentificacion/login.html',context={'login_form':form})

# funcion de logout
def logout(request):
    django_logout(request)
    messages.info(request, "Usuario delogueado")
    return redirect('login')