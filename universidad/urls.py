"""universidad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from uniapp.views import *
from estudiantes.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    # Carrera
    path('agregar_carrera/',nueva_carrera,name='nueva_carrera'),
    path('eliminar_carrera/<int:Codigo>',eliminar_carrera),
    path('editar_carrera/<int:Codigo>',editar_carrera),

    #Estudiantes
    path('estudiantes/',listado_estudiantes,name = 'estudiantes'),
    path('agregar_estudiante/', nuevo_estudiante,name = 'agregar'),
    path('estudiantes/eliminar_estudiante/<int:Cedula>',eliminar_estudiante),
]
