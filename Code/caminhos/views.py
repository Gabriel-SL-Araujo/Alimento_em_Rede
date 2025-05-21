from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def caminhos_home_1(request):
    return HttpResponse('<h1> Home01 <h1>')

def caminhos_home_2(request):
    return HttpResponse('<h1> Home02 <h1>')

def caminhos_sobre_1(request):
    return HttpResponse('<h1> sobre01 <h1>')

def caminhos_sobre_2(request):
    return HttpResponse('<h1> sobre02 <h1>')

def caminhos_login(request):
    return HttpResponse('<h1> login <h1>')

def caminhos_registro(request):
    return HttpResponse('<h1> registro <h1>')

def caminhos_perfil(request):
    return HttpResponse('<h1> perfil <h1>')