from django.shortcuts import render,redirect, get_object_or_404
from uniapp.models import Estudiantes
from .forms import EstudianteForm


# Create your views here.
def listado_estudiantes(request):
    estudiantes = Estudiantes.objects.all()
    num_estudiantes = Estudiantes.objects.count()
    return render(request,'index_estudiantes.html',
    {'estudiantes':estudiantes, 'num_estudiantes':num_estudiantes})

def nuevo_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudiantes')
    else:
        estudianteForm = EstudianteForm()
        return render(request,'agregar_estudiante.html',{'estudianteForm':estudianteForm})

def eliminar_estudiante(request, Cedula):
    estudiante = get_object_or_404(Estudiantes,pk=Cedula)

    if estudiante:
        estudiante.delete() 
    return redirect('estudiantes')
