from django.forms import ModelForm,TextInput
from uniapp.models import Estudiantes

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiantes
        fields = '__all__'
        widgets = {
            'Cedula': TextInput(attrs={'maxlength':'10'})
        }
