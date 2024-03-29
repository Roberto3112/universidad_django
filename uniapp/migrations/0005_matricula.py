# Generated by Django 4.1.3 on 2022-12-15 07:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uniapp', '0004_delete_matricula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('matricula', models.IntegerField(primary_key=True, serialize=False, verbose_name='Matricula')),
                ('Fecha_estudiante', models.DateField(verbose_name='Fecha de matricula')),
                ('Codigo_Carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uniapp.carrera')),
                ('id_Estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uniapp.estudiantes')),
            ],
        ),
    ]
