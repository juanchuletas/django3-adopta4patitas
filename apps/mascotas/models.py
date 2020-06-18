from django.db import models

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=10)
    image = models.ImageField(upload_to='adopciones/images')
    edad_aprox = models.IntegerField()
    sexo = models.CharField(max_length=20)
    fecha_rescate = models.DateField()
    fecha_adopcion = models.DateField(blank=True)
    descripcion = models.TextField(blank=False)
    def __str__(self):
        return '{}'.format(self.nombre)
