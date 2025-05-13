from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

TIPOS_USUARIO = (
    ('gerente', 'Gerente'),
    ('organizador', 'Organizador'),
)

class CustomUser(AbstractUser):
    tipo = models.CharField(max_length=20, choices=TIPOS_USUARIO)
    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.username

class EspacoEsportivo(models.Model):    
    nome = models.CharField(max_length=64)
    descricao = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=11, decimal_places=8)
    longitude = models.DecimalField(max_digits=12, decimal_places=8)
    cidade = models.CharField(max_length=64)
    UF = models.CharField(max_length=2)
    #foto_perfil = models.ImageField(upload_to="", verbose_name="Foto de Perfil")
    #foto_capa = models.ImageField(upload_to="./static/img", verbose_name="Capa de Perfil")
    media_avaliacao = models.DecimalField(max_digits=2, decimal_places=1, blank=True, default=0)
    #recursos_adicionais = models.TextField(blank=True, null=True) //Decidir se irá virar uma tabela ou um dicionario 
    #fotos = models.JSONField(default=list, blank=True, null=True) //Decidir se irá virar uma tabela excluisva para ou uma com fotos geral para o espaço e recurso, com um identificador para as ftos de capa e perfil
    #perguntas_respostas = models.TextField(blank=True, null=True)// Precisa explorar
    gerente = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'tipo': 'gerente'}, related_name="espacos")

    def __str__(self):
        return self.nome

class Recurso(models.Model):
    nome = models.CharField(max_length=255)
    foto_perfil = models.CharField(max_length=255, blank=True, null=True)
    #fotos = models.JSONField(default=list, blank=True, null=True)
    modalidade = models.CharField(max_length=100)
    espaco = models.ForeignKey(EspacoEsportivo, on_delete=models.CASCADE, related_name="recursos")

    def __str__(self):
        return f"Recurso {self.nome}"

class Agenda(models.Model):
    STATUS_CHOICES = [
        ("ativo", "Ativo"),
        ("inativo", "Inativo")
    ]
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    dia = models.DateField()
    h_inicial = models.TimeField()
    h_final = models.TimeField()
    recurso = models.ForeignKey(Recurso, on_delete=models.CASCADE, related_name="horarios")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="ativo")

    def __str__(self):
        return f"{self.dia} {self.h_inicial} - {self.h_final}"

class Reserva(models.Model):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("reservado", "Reservado"),
        ("cancelada", "Cancelada"),
        ("concluida", "Concluída"),
    ]
    organizador = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'tipo': 'organizador'})
    agenda = models.ForeignKey(Agenda, on_delete=models.CASCADE)
    nota_atendimento = models.IntegerField(null=True, blank=True)
    nota_recurso = models.IntegerField(null=True, blank=True)
    nota_limpeza = models.IntegerField(null=True, blank=True)
    comentario_avaliacao = models.TextField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True) 
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pendente")

    def __str__(self):
        return f"Reserva de {self.organizador.nome_completo} - {self.agenda.dia} ({self.status})"
