from django.urls import path
from .views import *

urlpatterns = [

    path("inicio/", inicio, name = "Inicio"),
    path("equipamiento/", ver_equipamiento, name = "VerEquipamiento"),
    path("servicios/", ver_servicios, name = "VerServicios"),
    path("entregas/", ver_estudio, name = "VerEstudio"),
    path("registrarse/", ver_registrarse, name="VerRegistrarse"),

    path("usuario/", crear_usuario, name = "CrearUsuario"),
]
