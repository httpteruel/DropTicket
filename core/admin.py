from django.contrib import admin
from .models import Evento, Lote, Excursao, Pedido, ItemPedido

class LoteInline(admin.TabularInline):
    model = Lote
    extra = 1

class ExcursaoInline(admin.TabularInline):
    model = Excursao
    extra = 1

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_inicio', 'local')
    search_fields = ('nome', 'local')
    inlines = [LoteInline, ExcursaoInline]

@admin.register(Excursao)
class ExcursaoAdmin(admin.ModelAdmin):
    list_display = ('evento', 'local_saida', 'vagas_totais', 'vagas_ocupadas', 'veiculo_tipo')
    list_filter = ('evento', 'local_saida')
    search_fields = ('local_saida',)

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0
    readonly_fields = ('lote', 'excursao', 'nome_participante', 'cpf_participante')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'status', 'total_pedido', 'data_criacao')
    list_filter = ('status', 'data_criacao')
    inlines = [ItemPedidoInline]

admin.site.register(Lote)
