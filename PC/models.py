from datetime import datetime
from django.db import models

class Usuario(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=32)
    email = models.EmailField()
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
    datainauguracao = models.DateField(null=True, blank=True)
    funcionamento = models.CharField(max_length=100)
    curiosidades = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to="img", null=True, blank=True)

    def __str__(self):
        return (self.nome)

class Comentario(models.Model):
    codigo = models.AutoField(primary_key=True)
    patrimonio = models.ForeignKey(Patrimonio, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    comentario = models.TextField()
    data = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return str(str(self.nome)+" - "+str(self.data))