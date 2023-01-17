from django.forms import ModelForm,TextInput,DateInput
from uniapp.models import Estudiantes

class EstudianteForm(ModelForm):
    class Meta:
        model = Estudiantes
        fields = '__all__'
        widgets = {
            'Cedula': TextInput(attrs={'maxlength':'10','required': True }),
            'FechaNacimiento': DateInput(attrs={'required': True, 'type': 'date'}),
            'Matricula': TextInput(attrs={'required':False })
        }
