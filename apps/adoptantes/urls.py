from django.urls import path
from apps.adoptantes.views import adopciones


urlpatterns = [
    path('listar/',adopciones,name='lista_adopciones'),
]
