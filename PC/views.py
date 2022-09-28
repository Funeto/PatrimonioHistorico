from django.shortcuts import render, redirect
from django.db.models.aggregates import Count
from datetime import datetime
from PC.models import *
from PC.forms import *

# Create your views here.

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

def createP(request):
    pacote = {}
    if request.method == "POST":
        form = PatrimonioForm(request.POST, request.FILES)
        if form.is_valid():
            obj = Patrimonio.objects.create(
                usuario = Usuario(codigo = 1),
                nome = form.cleaned_data.get("nome"),
                foto = form.cleaned_data.get("foto"),
                descricao = form.cleaned_data.get("descricao"),
                cidade = form.cleaned_data.get("cidade"),
                bairro = form.cleaned_data.get("bairro"),
                logradouro = form.cleaned_data.get("logradouro"),
                numero = form.cleaned_data.get("numero"),
                anoinauguracao = form.cleaned_data.get("anoinauguracao"),
                funcionamento = form.cleaned_data.get("funcionamento"),
                curiosidades = form.cleaned_data.get("curiosidades"),
            )
            obj.save()
            return redirect("/readPatrimonio")
    else:
        form = PatrimonioForm()
    pacote['form']= form
    return render(request, "createP.html", pacote)

def delP(request, id):
    patr = Patrimonio.objects.get(pk=id)
    patr.delete()
    return redirect("/readPatrimonio")

def updateP(request, id):
    patr = Patrimonio.objects.get(pk=id)
    form = PatrimonioModelForm(request.POST or None, instance=patr)
    if form.is_valid():
        form.save()
        return redirect("/readPatrimonio")
    pacote = {"form": form}
    return render(request, "createP.html", pacote)

def adminU(request):
    return render(request, "adminUser.html")

def createU(request):
    return render(request,'createUser.html')

def showU(request):
    return render(request,'showUser.html')

def index(request):
    patr = Patrimonio.objects.all()
    pacote = {"patrimonios": patr}
    return render(request, "index.html", pacote)

def login(request):
    return render(request,'login.html')