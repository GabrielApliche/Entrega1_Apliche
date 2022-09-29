from django.urls import path
from AppG.views import *


urlpatterns = [
   
    path('', inicio, name="Inicio"),
    path('libros/', libro, name="Libros"), 
    path('musicas/', musica, name="Musicas"), 
    path('peliculas/', pelicula, name="Peliculas"),    
    path('libroFormulario/', libroFormulario, name="FormularioLibro"),
    path('musicaFormulario/', musicaFormulario, name="FormularioMusica"),
    path('peliculaFormulario/', peliculaFormulario, name="FormularioPelicula"),
    #path('busquedaLibro/', busquedaLibro, name="BusquedaLibro"),
    path('resultadoLibro/', resultadoLibro, name="ResultadoLibro"),
    path('resultadoMusica/', resultadoMusica, name="ResultadoMusica"),
    path('resultadoPelicula/', resultadoPelicula, name="ResultadoPelicula"),
]