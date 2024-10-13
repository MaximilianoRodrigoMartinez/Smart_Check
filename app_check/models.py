from django.db import models

# Create your models here.


class Local(models.Model):

    nombre = models.CharField(max_length=20)

    def __str__(self):
     return self.nombre

class Empleado(models.Model):

    nombre = models.CharField(max_length=20)

    apellido = models.CharField(max_length=20, null=True, blank=True)

    puesto = models.CharField(max_length=20, null=True, blank=True)

    local = models.ForeignKey(Local, on_delete=models.CASCADE) 

    foto = models.ImageField(upload_to='empleados/', null=True, blank=True)  



    def __str__(self):
            return f"{self.nombre} {self.apellido} - {self.puesto} - {self.local}"

class Horario(models.Model):

    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)  
    
    hora_inicio = models.TimeField()
    
    hora_fin = models.TimeField()
    
    fecha = models.DateField()

    local = models.ForeignKey(Local, on_delete=models.CASCADE)


    def __str__(self):
        
     return f"{self.empleado} - {self.local} - {self.fecha}: {self.hora_inicio} a {self.hora_fin}"
    
















