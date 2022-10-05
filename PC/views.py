from rolepermissions.decorators import has_permission_decorator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
from django.db.models.aggregates import Count
from django.http import HttpResponse
from datetime import datetime
from PC.models import *
from PC.forms import *

# Create your views here.

@has_permission_decorator('remover_comentario')
def delC(request, idp, idc):
    comt = Comentario.objects.get(pk=idc)
    comt.delete()
    return redirect("/showPatrimonio/"+str(idp))

def showP(request, id):
    patr = Patrimonio.objects.get(pk=id)
    qtdComent = Comentario.objects.filter(patrimonio = id). aggregate(decla_count=Count ('*'))
    comt = Comentario.objects.filter(patrimonio = id)
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
    }
    return render(request,"showP.html", pacote)

def readP(request):
    patr = Patrimonio.objects.all()
    pacote = {"patrimonios": patr}  
    return render(request, "readP.html", pacote)

@has_permission_decorator('cadastrar_patrimonio')
def createP(request):
    pacote = {}
    if request.method == "POST":
        form = PatrimonioForm(request.POST, request.FILES)
        if form.is_valid():
            obj = Patrimonio.objects.create(
                usuario = Usuario(id = 1),
                nome = form.cleaned_data.get("nome"),
                foto = form.cleaned_data.get("foto"),
                descricao = form.cleaned_data.get("descricao"),
                cidade = form.cleaned_data.get("cidade"),
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
    patr.delete()
    return redirect("/readPatrimonio")

@has_permission_decorator('editar_patrimonio')
def updateP(request, id):
    patr = Patrimonio.objects.get(pk=id)
    form = PatrimonioModelForm(request.POST or None, request.FILES or None, instance=patr)
    if form.is_valid():
        form.save()
        return redirect("/readPatrimonio")
    pacote = {"form": form}
    return render(request, "createP.html", pacote)

@has_permission_decorator('conceder_permissao')
def adminU(request):
    return render(request, "adminUser.html")

@has_permission_decorator('cadastrar_usuario')
def createU(request):
    if request.method == "POST":
        first_name = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        senha_confirma = request.POST.get('senha_confirma')
        user = Usuario.objects.filter(username=email)
        if user.exists():
            return redirect("/createUsuario")
        elif senha != senha_confirma:
            return redirect("/createUsuario")
        user = Usuario.objects.create_user(username=email, email=email, password=senha, first_name=first_name, cidade="Caicó", tipo='S')
        user.save()
        return HttpResponse('Conta criada')

    return render(request,'createUser.html')

def showU(request):
    return render(request,'showUser.html')

def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(reverse('url_readP'))
        return render(request,'login.html')
    elif request.method == "POST":
        login = request.POST.get('email')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=login, password=senha)

        if not user:
            return HttpResponse('Usuário Inválido')

        auth.login(request, user)
        return redirect("/readPatrimonio")

def sair(request):
    request.session.flush()
    return redirect('/login')
    
def index(request):
    patr = Patrimonio.objects.all()
    pacote = {"patrimonios": patr}
    return render(request, "index.html", pacote)