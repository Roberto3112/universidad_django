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
from django.urls import path
from uniapp.views import *
from estudiantes.views import *
from cursos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),

    path('agregar_carrera/',nueva_carrera,name='nueva_carrera'),
    path('eliminar_carrera/<int:Codigo>',eliminar_carrera),
    path('editar_carrera/<int:Codigo>',editar_carrera),
    path('ver_estudiantes/<int:Codigo>', ver_estudiantes),

    #Estudiantes
    path('estudiantes/',listado_estudiantes,name = 'estudiantes'),
    path('agregar_estudiante/', nuevo_estudiante,name = 'agregar'),
    path('estudiantes/editar_estudiante/<int:Cedula>',editar_estudiante),
    path('estudiantes/eliminar_estudiante/<int:Cedula>',eliminar_estudiante),
    
    # Cursos
    path('ver_cursos/<int:Codigo>',ver_cursos),
    path('cursos',listado_cursos, name='cursos'),
    path('nuevo_curso',nuevo_curso, name='nuevo_curso'),
    path('editar_curso/<int:Codigo>',editar_curso),
    path('eliminar_curso/<int:Codigo>',eliminar_curso),
]
