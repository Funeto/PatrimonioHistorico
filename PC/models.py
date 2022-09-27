from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime
from django.db import models

class Usuario(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=32)
    email = models.CharField(max_length=100)
    senha = models.CharField(max_length=32)
    cidade = models.CharField(max_length=100)
    tipo = models.BooleanField()
    
    def __str__(self):
        return (self.nome)

class Patrimonio(models.Model):
    codigo = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField(max_length=400)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=16)
    anoinauguracao = models.IntegerField(validators=[MinValueValidator(-9999), MaxValueValidator(3000)])
    funcionamento = models.CharField(max_length=100)
    curiosidades = models.TextField(null=True)
    foto = models.ImageField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return (self.nome)

class Comentario(models.Model):
    codigo = models.AutoField(primary_key=True)
    patrimonio = models.ForeignKey(Patrimonio, on_delete=models.CASCADE)
    nome = models.CharField(max_length=32)
    comentario = models.CharField(max_length=32)
    data = models.DateTimeField(default=datetime.now(), blank=True)

    