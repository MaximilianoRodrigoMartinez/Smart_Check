from django import forms
from .models import Horario, Empleado, Local

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = ['empleado', 'hora_inicio', 'hora_fin', 'fecha']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'apellido', 'puesto', 'local', 'foto']

class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nombre'] 