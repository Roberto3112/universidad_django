from django.shortcuts import render,redirect, get_object_or_404
from uniapp.models import Carrera
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
    return render(request, 'agregar.html', { 'num_codigo':num_codigo})

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