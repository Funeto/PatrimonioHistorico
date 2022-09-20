from django.shortcuts import render

# Create your views here.
def showP(request):
    return render(request,"showP.html")

def readP(request):
    return render(request,"readP.html")

def adminU(request):
    return render(request, "adminUser.html")

def createP(request):
    return render(request,'createP.html')

def createU(request):
    return render(request,'createUser.html')

def showU(request):
    return render(request,'showUser.html')

def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')