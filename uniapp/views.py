from django.shortcuts import render,redirect, get_object_or_404
from uniapp.models import Carrera
from uniapp.forms import CarreraForm

# Create your views here.
#* Pagina principal
def index(request):
    carreras = Carrera.objects.all()
    total_carreras = Carrera.objects.count()
    return render(request, 'index.html',  {'carreras':carreras, 'total_carreras': total_carreras})

#* Registrar una nueva carrera
def nueva_carrera(request):
    carreraForm = CarreraForm()
     
    if request.method == 'POST':
        form = CarreraForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')

    else:
        carreraForm = CarreraForm()
    return render(request, 'agregar.html', {'carreraform':carreraForm})

#* Eliminar una carrera
def eliminar_carrera(request,Codigo):
    carrera = get_object_or_404(Carrera,pk=Codigo)

    if carrera:
        carrera.delete()
    return redirect('index')

#* Editar carrera
def editar_carrera(request,Codigo):
    carrera = get_object_or_404(Carrera,pk=Codigo)
    if request.method == 'POST':

        form = CarreraForm(request.POST,instance=carrera)
        if form.is_valid():
            form.save()
        return redirect('index')

    else:
        carreraForm = CarreraForm(instance=carrera)
    return render(request, 'editar.html', {'carreraform':carreraForm})