from django.forms import ModelForm, TextInput
from uniapp.models import Curso
from .funtions import codigo

class cursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'Codigo': TextInput(attrs={'type': 'number','value': codigo ,'readonly': True})
            }