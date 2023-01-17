from django.shortcuts import get_object_or_404
from uniapp.models import Estudiantes, Carrera
from datetime import datetime

def Matricula(codigo):
    carrera = get_object_or_404(Carrera,pk=codigo)
    estudiantes = Estudiantes.objects.all()
    year = datetime.now()
    num_estudiantes = 1
    for estudiante in estudiantes:
        if estudiante.CodigoCarrera_id == codigo:
            num_estudiantes += 1

    if codigo == carrera.Codigo:
        iniciales = ''

        for i in carrera.Nombre:
            iniciales += i 
            if len(iniciales) == 4 and iniciales == 'ING.':
                iniciales = ''
                for i in carrera.Nombre[5:9]:
                    iniciales += i
                hola = iniciales.upper()
            elif len(iniciales) == 4:
                hola = iniciales.upper()
        return f'{year.year}-{hola}-{num_estudiantes}' 
