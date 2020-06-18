from django.urls import path
from apps.mascotas.views import home, lista_mascotas, mapa_petfriendly,vet_list


urlpatterns = [
    path('',home,name="main_page"),
    path('mascotas/', lista_mascotas,name='mascotas_disponibles'),
    path('mapa/', mapa_petfriendly,name='lugares_petfriendly'),
    path('vets/',vet_list,name='lista_veterinarias'),
]
