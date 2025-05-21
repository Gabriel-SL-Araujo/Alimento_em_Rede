from django.urls import path
from caminhos.views import index, caminhos_home_2, caminhos_perfil, caminhos_login, caminhos_registro, caminhos_sobre_1, registrados
urlpatterns = [
    path('', index),
    path('nossos_projetos/', caminhos_home_2),
    path('quem_somos/', caminhos_sobre_1),
    path('login/', caminhos_login),
    path('registro/', caminhos_registro),
    path('perfil/', caminhos_perfil),
    path('registros/', registrados, name='listagem_usuarios'),
]