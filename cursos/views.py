from django.shortcuts import render,redirect,get_object_or_404
from .forms import cursoForm
from uniapp.models import *

# Create your views here.
#* Listado de cursos
def listado_cursos(request):
    cursos = Curso.objects.all()
    cant_cursos = Curso.objects.count()

    return render(request, 'cursos.html', {'cursos':cursos, 'cantidad':cant_cursos})

#* Agregar cursos
def nuevo_curso(request):

    if request.method == 'POST':
        form = cursoForm(request.POST)
        form.save()
        return redirect ('cursos')
    
    else:
        form = cursoForm()
    return render(request,'nuevo_curso.html',{'form':form})

#* Editar un curso
def editar_curso(request,Codigo):
    curso = get_object_or_404(Curso, pk=Codigo)
    if request.method == 'POST':
        form = cursoForm(request.POST,instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos')
    else: 
        form = cursoForm(instance=curso)
    return render(request, 'editar_curso.html', {'form':form})

def eliminar_curso(Codigo):
    curso = get_object_or_404(Curso, pk=Codigo)
    if curso:
        curso.delete()
    return redirect('cursos')