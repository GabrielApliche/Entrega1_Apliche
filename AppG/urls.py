from django.urls import path
from AppG.views import *


urlpatterns = [
   
    path('', inicio, name="Inicio"),
    path('libros/', libro, name="Libros"), 
    path('musicas/', musica, name="Musicas"), 
    path('peliculas/', pelicula, name="Peliculas"),    
   
]