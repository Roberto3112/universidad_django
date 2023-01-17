# Generated by Django 4.1.3 on 2022-12-16 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uniapp', '0005_matricula'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matricula',
            name='Codigo_Carrera',
        ),
        migrations.RemoveField(
            model_name='matricula',
            name='id_Estudiante',
        ),
        migrations.AddField(
            model_name='curso',
            name='carrera',
            field=models.ManyToManyField(to='uniapp.carrera'),
        ),
        migrations.DeleteModel(
            name='Estudiantes',
        ),
        migrations.DeleteModel(
            name='Matricula',
        ),
    ]
