# Generated by Django 5.1.1 on 2024-10-13 02:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(blank=True, max_length=20, null=True)),
                ('puesto', models.CharField(blank=True, max_length=20, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='empleados/')),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('fecha', models.DateField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_check.empleado')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_check.local')),
            ],
        ),
        migrations.AddField(
            model_name='empleado',
            name='local',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_check.local'),
        ),
    ]
