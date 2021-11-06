from django.db import models
from django.conf import settings

# Create your models here.
class Cidade(models.Model):
    nome = models.CharField(max_length=100,blank=False, default='')
    uf = models.CharField(max_length=2,blank=False, default='')


class Aeroporto(models.Model):
    nome = models.CharField(max_length=100, blank=False, default='')
    idCidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)


class Conexao(models.Model):
    class Meta:
        unique_together = (('idAeroportoOrigem', 'idAeroportoDestino'),)
    idAeroportoOrigem = models.ForeignKey(Aeroporto, on_delete=models.CASCADE, related_name='conexao_aeroporto_origem')
    idAeroportoDestino = models.ForeignKey(Aeroporto, on_delete=models.CASCADE, related_name='conexao_aeroporto_destino')


class Voo(models.Model):
    idAeroportoOrigem = models.ForeignKey(Aeroporto, on_delete=models.CASCADE, related_name='voo_aeroporto_origem')
    idAeroportoDestino = models.ForeignKey(Aeroporto, on_delete=models.CASCADE, related_name='voo_aeroporto_destino')
    assentos = models.IntegerField(default=0)
    preco = models.FloatField(default=0.0)
    data = models.DateField(blank=False)


class Compra(models.Model):
    idVoo = models.ForeignKey(Voo, on_delete=models.CASCADE)
    idUsuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=0)
    cancelada = models.BooleanField(default=False, blank=False)
    eticket = models.CharField(max_length=1000,blank=False, default='')