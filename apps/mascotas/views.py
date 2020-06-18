from django.shortcuts import render
from django.http import HttpResponse
from apps.mascotas.models import Mascota
# Create your views here.

def home(request):
    return render(request,'base_templates/home.html')
def lista_mascotas(request):
    mascota = Mascota.objects.all()
    contexto = {"datos_mascota":mascota}
    return render(request,'mascotas/listar_mascotas.html',contexto)
def mapa_petfriendly(request):
    return render(request,'mascotas/petfriendly.html')
def vet_list(request):
    return render(request,'mascotas/veterinaria.html')
