from django.db import models
from .choices import Sexo_choices, Vigencia_choices


# Create your models here.
class Carrera(models.Model):
    Codigo = models.IntegerField(primary_key=True)
    Nombre = models.CharField(max_length=100)
    Duracion = models.IntegerField(max_length=10)

    def __str__(self) -> str:
        return f'Codigo: {self.Codigo} Nombre: {self.Nombre} Duración: {self.Duracion}'

#* Estudiantes
class Estudiantes(models.Model):
    Cedula = models.IntegerField(primary_key=True,verbose_name='Cédula')
    Apellido_paterno = models.CharField(max_length=15,verbose_name='Apellido Materno')
    Apellido_materno = models.CharField(max_length=15,verbose_name='Apellido paterno')
    Nombres = models.CharField(max_length=50,verbose_name='Nombres')
    FechaNacimiento = models.DateField(max_length=15,verbose_name='Fecha de nacimiento')
    sexo = models.CharField(max_length=1,choices=Sexo_choices,verbose_name='Sexo')
    CodigoCarrera = models.ForeignKey(Carrera, on_delete=models.CASCADE,verbose_name='Codigo de carrera')
    Vigencia = models.IntegerField(choices=Vigencia_choices,verbose_name='Vigencia')

    def __str__(self) -> str:
        return f'Estudiante: {self.Nombres} {self.Apellido_paterno} {self.Apellido_materno}'

#* Curso
class Curso(models.Model):
    Codigo = models.IntegerField(primary_key=True, verbose_name='Codigo')
    Nombre = models.CharField(max_length=30,verbose_name='Nombre')
    Creditos = models.IntegerField(max_length=1,verbose_name='Creditos')
    Docente = models.CharField(max_length=100, verbose_name='Docente')

    def __str__(self) -> str:
        return f'Curso: {self.Nombre}, docente: {self.Docente}'
        
#* Matricula
class Matriculas(models.Model):
    id_Estudiante = models.ForeignKey(Estudiantes, on_delete=models.CASCADE)
    Codigo_Curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    Fecha_estudiante = models.DateField(verbose_name='Fecha de matricula')