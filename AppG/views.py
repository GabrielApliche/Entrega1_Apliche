
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppG.models import *


def inicio(request):
    
    return render(request, "AppG/inicio.html")

def libro(request):
    return render(request, "AppG/libro.html")

def musica(request):
    return render(request, "AppG/musica.html")

def pelicula(request):
    return render(request, "AppG/pelicula.html")

