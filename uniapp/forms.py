from django.forms import ModelForm,TextInput
from  uniapp.models import Carrera
from .funcions import codigo
import threading


class CarreraForm(ModelForm):
    class Meta:
        model = Carrera
        fields = ['Nombre','Duracion', 'Codigo']
        widgets = {
        'Codigo' : TextInput(attrs={'type':'number','value':codigo()})
        }

