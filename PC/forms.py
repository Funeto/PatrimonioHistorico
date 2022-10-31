from django import forms as django_forms
from django.contrib.auth import forms 
from PC.models import Patrimonio, Usuario
from django.forms import ModelForm

class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = Usuario

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Usuario

class PatrimonioForm(django_forms.Form):
    nome = django_forms.CharField(max_length=100, label="Nome do patrimônio:")
    descricao = django_forms.CharField(widget=django_forms.Textarea, max_length=400, label="Descrição:")
    bairro = django_forms.CharField(max_length=100, label="Bairro:")
    logradouro = django_forms.CharField(max_length=100, label="Logradouro:")
    numero = django_forms.CharField(max_length=16, label="Número:")
    datainauguracao = django_forms.DateField(label="Data de inauguração:", required=False)
    funcionamento = django_forms.CharField(max_length=100, label="Horário de funcionamento:")
    curiosidades = django_forms.CharField(widget=django_forms.Textarea, label="Curiosidades:", required=False)
    foto = django_forms.ImageField(label="Escolha uma foto:")

class PatrimonioModelForm(ModelForm):
    class Meta:
        model = Patrimonio
        fields = ('nome', 'descricao', 'bairro', 'logradouro', 'numero', 'datainauguracao', 'funcionamento', 'curiosidades', 'foto')
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

class ComentarioForm(django_forms.Form):
    nome = django_forms.CharField(max_length=100, label="Seu nick:")
    email = django_forms.EmailField(label="E-mail:")
    comentario = django_forms.CharField(widget=django_forms.Textarea, max_length=1000, label="Comentário:")

    