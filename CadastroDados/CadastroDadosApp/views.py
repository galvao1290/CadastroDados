from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Dados

# Create your views here.

def home(request):
    return render(request, 'index.html')

def enviar_dados(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        if nome and idade:
            Dados.objects.create(nome=nome,idade=idade)
            
    return redirect('home')
    

def dados(request):
    dados = Dados.objects.values('id', 'nome', 'idade')
    return render(request, 'dados.html', {'dados': dados})