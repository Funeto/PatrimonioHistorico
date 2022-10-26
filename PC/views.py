from math import perm
from rolepermissions.decorators import has_permission_decorator
from rolepermissions.permissions import revoke_permission, grant_permission
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import auth
from django.db.models.aggregates import Count
from datetime import datetime
from PC.models import *
from PC.forms import *
import random

cida = Cidade.objects.all()

# permissão para nenhum usuário logado mexer em um patrimônio que não é de sua cidade
def permissaoM(request, obj):
    if request.user.is_authenticated:
        current_user = request.user
        if current_user.tipo == "S" or current_user.tipo == "A":
            if current_user.cidade == obj.cidade or current_user.cidade == None:
                return True
    else:
        return False

@has_permission_decorator('remover_comentario')
def delC(request, idp, idc):
    comt = Comentario.objects.get(pk=idc)
    objp = Patrimonio.objects.get(pk=idp)
    permissao = False
    if permissaoM(request=request, obj=objp) == True:
        permissao = True
        comt.delete()
    return redirect("/showPatrimonio/"+str(idp))
    

def showP(request, id):
    permissao = False
    patr = Patrimonio.objects.get(pk=id)
    qtdComent = Comentario.objects.filter(patrimonio = id). aggregate(decla_count=Count ('*'))
    comt = Comentario.objects.filter(patrimonio = id)
    # esse if limita o usuário logado mexer em um patrimônio que não é de sua cidade
    if permissaoM(request=request, obj=patr) == True:
        permissao = True
    if request.method == "POST":
        form = ComentarioForm(request.POST, request.FILES)
        if form.is_valid():
            obj = Comentario.objects.create(
                patrimonio = Patrimonio(codigo = id),
                nome = form.cleaned_data.get("nome"),
                comentario = form.cleaned_data.get("comentario"),
                data = datetime.now(),
            )
            obj.save()
            return redirect("/showPatrimonio/"+str(id))
    else:
        form = ComentarioForm()
    pacote = {
        "patrimonio": patr,
        "form": form,
        "qtdComent": qtdComent,
        "comentarios": comt,
        "cidades": cida,
        "permissao": permissao,
    }
    return render(request,"showP.html", pacote)

def verP(request, id):
    # esse if limita o usuário logado mexer em um patrimônio que não é de sua cidade
    permissao = False
    if request.user.is_authenticated:
        current_user = request.user
        if current_user.tipo == "S" or current_user.tipo == "A":
            if current_user.cidade == Cidade.objects.get(id = id) or current_user.cidade == None:
                permissao = True
    patr = Patrimonio.objects.filter(cidade = Cidade.objects.get(id = id))
    pacote = {"patrimonios": patr, "cidades": cida, "permissao": permissao}
    return render(request, "readP.html", pacote)

def readP(request):
    permissao = True
    if request.user.is_authenticated:
        current_user = request.user
        if current_user.tipo == "S" or current_user.tipo == "A":
            patr = Patrimonio.objects.filter(cidade = current_user.cidade)
    else:
        return redirect("/")
    pacote = {"patrimonios": patr, "cidades": cida, "permissao": permissao}
    return render(request, "readP.html", pacote)

@has_permission_decorator('cadastrar_patrimonio')
def createP(request):
    pacote = {}
    current_user = request.user
    if request.method == "POST":
        form = PatrimonioForm(request.POST, request.FILES)
        if form.is_valid():
            obj = Patrimonio.objects.create(
                usuario = current_user,
                nome = form.cleaned_data.get("nome"),
                foto = form.cleaned_data.get("foto"),
                descricao = form.cleaned_data.get("descricao"),
                cidade = current_user.cidade,
                bairro = form.cleaned_data.get("bairro"),
                logradouro = form.cleaned_data.get("logradouro"),
                numero = form.cleaned_data.get("numero"),
                datainauguracao = form.cleaned_data.get("datainauguracao"),
                funcionamento = form.cleaned_data.get("funcionamento"),
                curiosidades = form.cleaned_data.get("curiosidades"),
            )
            obj.save()
            return redirect("/readPatrimonio")
    else:
        form = PatrimonioForm()
    pacote['form']= form
    return render(request, "createP.html", pacote)

@has_permission_decorator('remover_patrimonio')
def delP(request, id):
    patr = Patrimonio.objects.get(pk=id)
    if permissaoM(request=request, obj=patr) == True:
        patr.delete()
    return redirect("/readPatrimonio")

@has_permission_decorator('editar_patrimonio')
def updateP(request, id):
    update =True
    patr = Patrimonio.objects.get(pk=id)
    if permissaoM(request=request, obj=patr) == True:
        form = PatrimonioModelForm(request.POST or None, request.FILES or None, instance=patr)
        if form.is_valid():
            form.save()
            return redirect("/readPatrimonio")
        pacote = {"form": form, "update":update}
        return render(request, "createP.html", pacote)
    else:
        return redirect("/readPatrimonio")

@has_permission_decorator('conceder_permissoes')
def adminU(request):
    current_user = request.user
    users = Usuario.objects.filter(cidade=current_user.cidade, tipo='S')
    pacote = {"users": users}
    return render(request, "adminUser.html", pacote)

@has_permission_decorator('conceder_permissoes')
def revogarCP(request,id):
    user = Usuario.objects.get(pk=id)
    revoke_permission(user, 'cadastrar_patrimonio')
    return redirect("/adminUsuario")

@has_permission_decorator('conceder_permissoes')
def revogarEP(request,id):
    user = Usuario.objects.get(pk=id)
    revoke_permission(user, 'editar_patrimonio')
    return redirect("/adminUsuario")

@has_permission_decorator('conceder_permissoes')
def revogarDP(request,id):
    user = Usuario.objects.get(pk=id)
    revoke_permission(user, 'remover_patrimonio')
    return redirect("/adminUsuario")

@has_permission_decorator('conceder_permissoes')
def revogarDC(request,id):
    user = Usuario.objects.get(pk=id)
    revoke_permission(user, 'remover_comentario')
    return redirect("/adminUsuario")

@has_permission_decorator('conceder_permissoes')
def concederCP(request,id):
    user = Usuario.objects.get(pk=id)
    grant_permission(user, 'cadastrar_patrimonio')
    return redirect("/adminUsuario")

@has_permission_decorator('conceder_permissoes')
def concederEP(request,id):
    user = Usuario.objects.get(pk=id)
    grant_permission(user, 'editar_patrimonio')
    return redirect("/adminUsuario")

@has_permission_decorator('conceder_permissoes')
def concederDP(request,id):
    user = Usuario.objects.get(pk=id)
    grant_permission(user, 'remover_patrimonio')
    return redirect("/adminUsuario")

@has_permission_decorator('conceder_permissoes')
def concederDC(request,id):
    user = Usuario.objects.get(pk=id)
    grant_permission(user, 'remover_comentario')
    return redirect("/adminUsuario")

@has_permission_decorator('cadastrar_usuarios_aux')
def createU(request):
    if request.method == "POST":
        current_user = request.user
        first_name = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha_confirma = request.POST.get('senha_confirma')
        user = Usuario.objects.filter(username=email)
        if user.exists():
            texto = "Email ou senha inválidos"
            mensagem = {"texto":texto}
            return render(request, "createUser.html", mensagem)
        elif senha != senha_confirma:
            return redirect("/createUsuario")
        user = Usuario.objects.create_user(username=email, email=email, password=senha, first_name=first_name, cidade=current_user.cidade, tipo='S')
        user.save()
        return redirect("/adminUsuario")

    return render(request,'createUser.html')

def showU(request,id):
    usuario = Usuario.objects.get(pk=id)
    pacote = {"usuario":usuario}
    return render(request,'showUser.html', pacote)

def delU(request, id):
    usuario = Usuario.objects.get(pk=id)
    usuario.delete()
    return redirect("/adminUsuario")

def login(request):
    pacote = {"cidades": cida}
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('url_readP'))
        return render(request,'login.html', pacote)
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)

        if not user:
            texto = "Email ou senha inválidos"
            mensagem = {"texto":texto}
            return render(request, 'login.html', mensagem)

        auth.login(request, user)
        return redirect("/readPatrimonio")

def sair(request):
    request.session.flush()
    return redirect('/login')
    
def index(request):
    patrPesquisa = Patrimonio.objects.all()
    itens = list(patrPesquisa)
    random_items = random.sample(itens, 6)
    search = request.GET.get('search')
    pacote = {"patrimonios": patrPesquisa, "cidades": cida, "aleatorio": random_items}
    if search:
        patrPesquisa = patrPesquisa.filter(nome__icontains=search)
        pacote = {"patrimonios": patrPesquisa, "cidades": cida, "aleatorio": random_items}
        return render(request, "readP.html", pacote)
    return render(request, "index.html", pacote)

def handler404(request, exception):
    return redirect("/")

class Redefinir(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('url_readP')
