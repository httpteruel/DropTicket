from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Evento(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Evento")
    data_inicio = models.DateTimeField(verbose_name="Início do Evento")
    data_fim = models.DateTimeField(verbose_name="Término do Evento")
    local = models.CharField(max_length=255, verbose_name="Local/Endereço")
    descricao = models.TextField(verbose_name="Descrição do Evento")
    banner = models.ImageField(upload_to='eventos/', null=True, blank=True, verbose_name="Banner/Poster")
    contato_organizador = models.CharField(max_length=100, verbose_name="Contato do Organizador")

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"

    def __str__(self):
        return self.nome

class Lote(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='lotes')
    nome_lote = models.CharField(max_length=100, verbose_name="Tipo/Lote (Ex: Pista 1º Lote)")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço")
    quantidade_total = models.PositiveIntegerField(verbose_name="Qtd Total de Ingressos")
    quantidade_vendida = models.PositiveIntegerField(default=0, verbose_name="Vendidos")
    ativo = models.BooleanField(default=True, verbose_name="Lote Ativo?")

    def __str__(self):
        return f"{self.evento.nome} - {self.nome_lote}"

class Excursao(models.Model):
    TIPO_VEICULO = [('VAN', 'Van'), ('BUS', 'Ônibus'), ('MICRO', 'Micro-ônibus')]
    
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='excursoes')
    responsavel = models.CharField(max_length=100, verbose_name="Nome do Responsável")
    contato = models.CharField(max_length=20, verbose_name="WhatsApp/Telefone")
    local_saida = models.CharField(max_length=255, verbose_name="Local de Embarque")
    data_embarque = models.DateTimeField(verbose_name="Data/Hora Ida")
    data_retorno = models.DateTimeField(verbose_name="Data/Hora Retorno")
    vagas_totais = models.PositiveIntegerField(verbose_name="Total de Assentos")
    vagas_ocupadas = models.PositiveIntegerField(default=0, verbose_name="Assentos Ocupados")
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Preço da Vaga")
    veiculo_tipo = models.CharField(max_length=10, choices=TIPO_VEICULO, default='BUS')
    veiculo_placa = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name = "Excursão"
        verbose_name_plural = "Excursões"

    def __str__(self):
        return f"Excursão {self.local_saida} ({self.evento.nome})"

class Pedido(models.Model):
    STATUS_CHOICES = [('P', 'Pendente'), ('PAGO', 'Pago'), ('C', 'Cancelado')]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Comprador")
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_pagamento = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='P')
    total_pedido = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def pode_cancelar(self, data_evento_inicio):
        """
        Lógica: Pode cancelar em até 3 dias após o pagamento, 
        desde que não falte menos de 3 dias para o evento.
        """
        if not self.data_pagamento or self.status == 'C':
            return False
            
        agora = timezone.now()
        prazo_apos_pagamento = self.data_pagamento + timedelta(days=3)
        prazo_limite_evento = data_evento_inicio - timedelta(days=3)
        
        return agora <= prazo_apos_pagamento and agora < prazo_limite_evento

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    # Pode ser um ingresso de lote OU uma vaga em excursão
    lote = models.ForeignKey(Lote, on_delete=models.SET_NULL, null=True, blank=True)
    excursao = models.ForeignKey(Excursao, on_delete=models.SET_NULL, null=True, blank=True)
    
    # Dados de quem vai usar (para a Lista de Passageiros/Ingresso)
    nome_participante = models.CharField(max_length=150)
    cpf_participante = models.CharField(max_length=14)
    email_participante = models.EmailField()
    qr_code_key = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        tipo = "Ingresso" if self.lote else "Excursão"
        return f"{tipo}: {self.nome_participante}"