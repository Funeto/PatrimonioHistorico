from django import forms
from PC.models import Patrimonio
from django.forms import ModelForm

class PatrimonioForm(forms.Form):
    nome = forms.CharField(max_length=100, label="Nome do patrimônio:")
    descricao = forms.CharField(widget=forms.Textarea, max_length=400, label="Descrição:")
    cidade = forms.CharField(max_length=100, label="Cidade:")
    bairro = forms.CharField(max_length=100, label="Bairro:")
    logradouro = forms.CharField(max_length=100, label="Logradouro:")
    numero = forms.CharField(max_length=16, label="Número:")
    datainauguracao = forms.DateField(label="Data de inauguração:", required=False)
    funcionamento = forms.CharField(max_length=100, label="Horário de funcionamento:")
    curiosidades = forms.CharField(widget=forms.Textarea, label="Curiosidades:", required=False)
    foto = forms.ImageField(label="Escolha uma foto:")

class PatrimonioModelForm(ModelForm):
    class Meta:
        model = Patrimonio
        fields = ('nome', 'descricao', 'cidade', 'bairro', 'logradouro', 'numero', 'datainauguracao', 'funcionamento', 'curiosidades', 'foto')
        labels = {
            "nome": "Nome do patrimônio:",
            "descricao": "Descrição:",
            "cidade": "Cidade:",
            "bairro": "Bairro:",
            "logradouro": "Logradouro:",
            "numero": "Número:",
            "datainauguracao": "Data de inauguração:",
            "funcionamento": "Horário de funcionamento:",
            "curiosidades": "Curiosidades:",
            "foto": "Escolha uma foto:",
        }

class ComentarioForm(forms.Form):
    nome = forms.CharField(max_length=100, label="Seu nick:")
    email = forms.EmailField(label="E-mail:")
    comentario = forms.CharField(widget=forms.Textarea, max_length=1000, label="Comentário:")

    