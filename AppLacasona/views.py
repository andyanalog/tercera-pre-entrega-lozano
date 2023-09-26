from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import ProfesorFormulario
# Create your views here.

def inicio(request):
    a = 20
    return render(request,"AppLacasona/inicio.html")

def ver_equipamiento(request):
    return render(request,"AppLacasona/ver_equipamiento.html")

def ver_servicios(request):
    return render(request,"AppLacasona/ver_servicios.html")

def ver_estudio(request):
    return render(request,"AppLacasona/ver_estudio.html")

def ver_registrarse(request):
    return render(request,"AppLacasona/ver_registrarse.html")

def crear_usuario(request):

    if request.method == "POST": #al persionar el botón
        usuario_nuevo = Usuario(nombre=request.POST["nombre"], comision=request.POST["comision"])
        usuario_nuevo.save()
        return render(request,"AppLacasona/inicio.html")
    
    return render(request, "AppLacasona/crear_usuario.html")


def crear_profes(request):

    if request.method == "POST": #al persionar el botón

        miFormulario = ProfesorFormulario(request.POST)
        if miFormulario.is_valid:
            info = miFormulario.cleaned_data
            profe_nuevo = Profesor(nombre=info["nombre"], apellido=info["apellido"], email=info["email"])
            profe_nuevo.save()
        return render(request,"AppLacasona/inicio.html")
    
    else:
        miFormulario = ProfesorFormulario()
    
    return render(request, "AppLacasona/crear_usuario.html")

"""
def profe_nuevo(request):
    profeN = Profesor(nombre = "Pepe", apellido = "pipi", email = "pepe@pipi.com")
    profeN.save()

    return HttpResponse(f"Hemos guardado al profesor {profeN.nombre}")

def curso_nuevo(request):
    curso_favorito = Curso(nombre = "Python", comision = "47765")
    curso_favorito.save()

    return HttpResponse(f"Bienvenidos al curso {curso_favorito.nombre}")
"""