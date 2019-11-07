from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

    
def exibir(request):
    return render(request, 'exibir.html')

def login(request):
    return render(request, 'login.html')

def cadastrar(request):
    return render(request, 'cadastrar.html')