from django import forms

class LibroFormulario(forms.Form):
    nombre = forms.CharField()
    autor = forms.CharField()
    publicacion = forms.IntegerField()

class MusicaFormulario(forms.Form):
    cancion = forms.CharField()
    disco = forms.CharField()
    grupo = forms.CharField()
    año = forms.IntegerField()

class PeliculaFormulario(forms.Form):
    nombre = forms.CharField()
    director = forms.CharField()
    año = forms.IntegerField()