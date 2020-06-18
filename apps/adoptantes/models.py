from django.db import models

# Create your models here.
class Adoptante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    direccion = models.TextField()
    image = models.ImageField(upload_to='adoptantes/images',default='DEFAULT VALUE')

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellido)
