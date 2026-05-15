from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Evento, Lote, Excursao

class EventoListView(ListView):
    model = Evento
    template_name = 'index.html' 
    context_object_name = 'eventos'
    ordering = ['data_inicio']     

class EventoDetailView(DetailView):
    model = Evento
    template_name = 'detalhe_evento.html'
    context_object_name = 'evento'
    slug_field = 'slug'       
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        """
        Método obrigatório exigido pelo professor para passar dados adicionais
        (Lotes de ingressos e Excursões disponíveis para este evento específico).
        """
        context = super().get_context_data(**kwargs)
        context['lotes'] = self.object.lotes.filter(ativo=True)
        context['excursoes'] = self.object.excursoes.all()
        return context

class EventoCreateView(CreateView):
    model = Evento
    fields = ['nome', 'slug', 'data_inicio', 'data_fim', 'local', 'descricao', 'banner', 'contato_organizador']
    template_name = 'evento_form.html'
    success_url = reverse_lazy('evento_list')

class EventoUpdateView(UpdateView):
    model = Evento
    fields = ['nome', 'slug', 'data_inicio', 'data_fim', 'local', 'descricao', 'banner', 'contato_organizador']
    template_name = 'evento_form.html'
    success_url = reverse_lazy('evento_list')
