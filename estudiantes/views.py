from django.shortcuts import render,redirect, get_object_or_404
from uniapp.models import Estudiantes,Carrera
from .forms import EstudianteForm
from .funtions import Matricula

# Create your views here.
def listado_estudiantes(request):
    estudiantes = Estudiantes.objects.all()
    num_estudiantes = Estudiantes.objects.count()
    return render(request,'index_estudiantes.html',
    {'estudiantes':estudiantes, 'num_estudiantes':num_estudiantes})

def nuevo_estudiante(request):
    carreras = Carrera.objects.all()

    # Recuperar los valores
    if request.method == 'POST':
        cedula = request.POST.get('Cedula')
        apellido_p = request.POST.get('Apellido_paterno')
        apellido_m = request.POST.get('Apellido_materno')
        nombres = request.POST.get('Nombres')
        fecha_n = request.POST.get('fecha_nacimiento')
        sexo = request.POST.get('sexo')
        vigencia = request.POST.get('Vigencia')
        codigocarrera = request.POST.get('CodigoCarrera')
        matricula = Matricula(int(codigocarrera))
        
        # print(codigocarrera)
        # print(Carrera.objects.get(pk=codigocarrera))
        # Una idea para la matricula es obtener el codigo de la carrera luego crear un objeto con el id de la carrera
        # Para luego definir que con ese objeto recueperemos el nombre y creamos la funcion de obtener la matricula
        
        nuevo_estudiante = Estudiantes.objects.create(Matricula = matricula, Cedula = cedula, 
        Apellido_paterno = apellido_p, Apellido_materno = apellido_m, Nombres = nombres, FechaNacimiento = fecha_n,
        sexo = sexo, Vigencia = vigencia, CodigoCarrera_id = codigocarrera)

        nuevo_estudiante.save()
        return redirect('estudiantes')
    else:
        estudianteForm = EstudianteForm()
    return render(request,'agregar_estudiante.html',{'estudianteForm':estudianteForm, 'carreras': carreras})

def editar_estudiante(request, Cedula):
    estudiante = get_object_or_404(Estudiantes,pk=Cedula)
    form = EstudianteForm(instance=estudiante)
    if request.method == 'POST':
        form = EstudianteForm(request.POST,instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('estudiantes')          
    return render(request,'editar_estudiante.html',{'form':form})

def eliminar_estudiante(request, Cedula):
    estudiante = get_object_or_404(Estudiantes,pk=Cedula)

    if estudiante:
        estudiante.delete() 
    return redirect('estudiantes')

    