from django.shortcuts import render
from django.http import HttpResponse
from apps.adoptantes.models import Adoptante

# Create your views here.

def adopciones(request):
    adop= Adoptante.objects.all()
    contexto = {"datos_adoptante":adop}
    return render(request,'adoptantes/listar_adopciones.html',contexto)
