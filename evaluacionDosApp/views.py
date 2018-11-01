from django.shortcuts import render
from .models import Automovil
from .froms import RegistroForm
from django.utils import timezone
# Create your views here.

# def formu(request):
#     form = RegistroForm()
#     context = {
#         "form": form,
#     }
#     return render(request, "registro.html", context)

def index(request):
    # automovil = Automovil.objects.filter(FechaPublicacion__lte = timezone.now()).order_by('FechaPublicacion')
    form = RegistroForm()
    context = {
        "form": form,
    }
    return render(request, 'evaluacionDosAPP/registro.html', context)

# def ultimo(request):
#     p = Automovil.objects.order_by('Fecha_publicacion').first()
#     context = {'automo'}
