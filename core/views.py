from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Evento

def home(request):
    eventos = Evento.objects.all() # Busca por todos os eventos
    return render(request, 'index.html', {'eventos': eventos})

def detalhe_evento(request, evento_id):
    # Busca pelo ID
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'detalhe_evento.html', {'evento': evento})