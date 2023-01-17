from django.shortcuts import render,redirect, get_object_or_404
from uniapp.models import Carrera,Estudiantes,Curso
from uniapp.forms import CarreraForm
from .funcions import codigo

# Create your views here.
#* Pagina principal
def index(request):
    carreras = Carrera.objects.all()
    total_carreras = Carrera.objects.count()
    return render(request, 'index.html',  {'carreras':carreras, 'total_carreras': total_carreras})

#* Registrar una nueva carrera
def nueva_carrera(request):

    if request.method == 'POST':
        # Para recuperar los valores y enviarlos a la bd
        code = request.POST.get('Codigo')
        nombre = request.POST.get('Nombre')
        duracion = request.POST.get('Duracion')
        nueva_carrera = Carrera.objects.create(Codigo =code, Nombre= nombre, Duracion= duracion)
        nueva_carrera.save()
        return redirect('index')

    else:
        num_codigo = codigo()  
    return render(request, 'agregar.html',{'num_codigo':num_codigo})

#* Eliminar una carrera
def eliminar_carrera(request,Codigo):
    carrera = get_object_or_404(Carrera,pk=Codigo)

    if carrera:
        carrera.delete()
    return redirect('index')

#* Editar carrera
def editar_carrera(request,Codigo):
      
    carrera = get_object_or_404(Carrera, pk=Codigo)
    if request.method == 'POST':
        form = CarreraForm(request.POST,instance=carrera)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        carreraForm = CarreraForm(instance=carrera)
    return render(request, 'editar.html', {'carreraForm':carreraForm})

def ver_estudiantes(request, Codigo):
    carrera = get_object_or_404(Carrera, pk=Codigo)
    estudiantes = Estudiantes.objects.all()

    # Para saber si hay o no hay estudiantes en una carrera
    lista = []
    for estudiante in estudiantes:
        if estudiante.CodigoCarrera_id == carrera.Codigo:
            lista.append(estudiante)

    return render(request, 'ver_estudiantes.html',{'carrera':carrera, 'estudiantes':estudiantes, 'listaEstudiantes': lista})

#* Ver los cursos
def ver_cursos(request, Codigo):
    carreras = get_object_or_404(Carrera,pk=Codigo)
    cursos = Curso.carrera.through.objects.all()

# Hacer una funcion aparte para esto
    lista = []
    for c in cursos:
        # print(c.carrera)
        if c.carrera_id == carreras.Codigo:
            print(c.carrera_id)
            curso = get_object_or_404(Curso,pk=c.curso_id)
            lista.append(curso)
            print(lista)

    return render(request, 'ver_cursos.html', {'carrera': carreras,  'lista':lista})


