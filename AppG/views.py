
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppG.models import *
from AppG.forms import *


def inicio(request):
    
    return render(request, "AppG/inicio.html")

def libro(request):
    return render(request, "AppG/libro.html")

def musica(request):
    return render(request, "AppG/musica.html")

def pelicula(request):
    return render(request, "AppG/pelicula.html")


def libroFormulario(request):

    if request.method == "POST":

        formulario1 = LibroFormulario(request.POST)

        if formulario1.is_valid():
            
            info = formulario1.cleaned_data

            libro = Libro(nombre=info["nombre"], autor=info["autor"], publicacion=info["publicacion"])

            libro.save()

            return render(request, "AppG/inicio.html")

    else:

        formulario1 = LibroFormulario()  
        
     
    return render(request, "AppG/libroFormulario.html", {"form1":formulario1})


def musicaFormulario(request):
    
    if request.method == "POST":

        formulario2 = MusicaFormulario(request.POST)

        if formulario2.is_valid():
            
            info = formulario2.cleaned_data

            musica = Musica(cancion=info["cancion"], disco=info["disco"], grupo=info["grupo"], año=info["año"])

            musica.save()

            return render(request, "AppG/inicio.html")

    else:

        formulario2 = MusicaFormulario()  
        
     
    return render(request, "AppG/musicaFormulario.html", {"form2":formulario2})


def peliculaFormulario(request):

    if request.method == "POST":

        formulario3 = PeliculaFormulario(request.POST)

        if formulario3.is_valid():
            
            info = formulario3.cleaned_data

            pelicula = Pelicula(nombre=info["nombre"], director=info["director"], año=info["año"])

            pelicula.save()

            return render(request, "AppG/inicio.html")

    else:

        formulario3 = PeliculaFormulario()  
        
     
    return render(request, "AppG/peliculaFormulario.html", {"form3":formulario3})


def busquedaLibro(request):
    return render(request, "AppG/libro.html")

def resultadoLibro(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
    
        libros = Libro.objects.filter(nombre__icontains=nombre)

        return render(request, "AppG/libro.html", {"libros":libros, "nombre":nombre})
    
    else:

        respuesta = "No enviaste datos."
        return HttpResponse(respuesta)
    #return render(request, "AppG/libro.html", {"respuesta":respuesta})

def resultadoMusica(request):

    if request.GET["cancion"]:

        cancion = request.GET["cancion"]
    
        musicas = Musica.objects.filter(cancion__icontains=cancion)

        return render(request, "AppG/musica.html", {"musicas":musicas, "cancion":cancion})
    
    else:

        respuesta = "No enviaste datos."
        return HttpResponse(respuesta)

def resultadoPelicula(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
    
        peliculas = Pelicula.objects.filter(nombre__icontains=nombre)

        return render(request, "AppG/pelicula.html", {"peliculas":peliculas, "nombre":nombre})
    
    else:

        respuesta = "No enviaste datos."
        return HttpResponse(respuesta)
    