from django.shortcuts import render
from .models import Registros
from django.shortcuts import redirect


def index(request):
    return render(request, 'index.html')


def caminhos_sobre_1(request):
    return render(request, 'sobre_1.html')


def caminhos_login(request):
    return render(request, 'login.html')

def caminhos_registro(request):
    if request.method == 'POST':
        novo_registro = Registros()
        novo_registro.nome = request.POST.get('nome')
        novo_registro.email = request.POST.get('email')
        novo_registro.senha = request.POST.get('senha')
        novo_registro.save()

    registros = {
        'registros': Registros.objects.all()
    }
    return render(request, 'registro.html')


def caminhos_perfil(request):
    return render(request, 'perfil.html')

