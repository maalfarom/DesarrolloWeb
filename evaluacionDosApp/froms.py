from django import forms
from django.forms import ComboField

class RegistroForm(forms.Form):
    Marca = forms.CharField()
    Modelo = forms.CharField()
    Anio = forms.IntegerField()
    color = forms.CharField()
    Descripcion = forms.CharField()
    Precio = forms.CharField()
