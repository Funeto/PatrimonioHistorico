import imp
from django import forms
from PC.models import Patrimonio
from django.forms import ModelForm

class PatrimonioForm(forms.Form):
    nome = forms.CharField(max_length=100, label="Nome do Patrimônio")
    descricao = forms.CharField(widget=forms.Textarea, max_length=400, label="Descrição")
    cidade = forms.CharField(max_length=100, label="Cidade")
    bairro = forms.CharField(max_length=100, label="Bairro")
    logradouro = forms.CharField(max_length=100, label="Logradouro")
    numero = forms.CharField(max_length=16, label="Número")
    anoinauguracao = forms.IntegerField(label="Ano de inauguração")
    funcionamento = forms.CharField(max_length=100, label="Horário de Funcionamento")
    curiosidades = forms.CharField(widget=forms.Textarea, label="Curiosidades")
    foto = forms.ImageField(label="Escolha uma foto")

class PatrimonioModelForm(ModelForm):
    class Meta:
        model = Patrimonio
        fields = ('nome', 'descricao', 'cidade', 'bairro', 'logradouro', 'numero', 'anoinauguracao', 'funcionamento', 'curiosidades', 'foto')

class ComentarioForm(forms.Form):
    nome = forms.CharField(max_length=100, label="Seu nick:")
    comentario = forms.CharField(widget=forms.Textarea, max_length=1000, label="Comentário:")

    