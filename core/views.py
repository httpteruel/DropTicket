from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Evento

def home(request):
    eventos = Evento.objects.all() # Busca todos os eventos do banco
    return render(request, 'index.html', {'eventos': eventos})

def detalhe_evento(request, evento_id):
    # Busca o evento pelo ID ou retorna erro 404 se não existir
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'detalhe_evento.html', {'evento': evento})