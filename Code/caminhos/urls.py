from django.urls import path
from caminhos.views import index, caminhos_home_1, caminhos_home_2, caminhos_perfil, caminhos_login, caminhos_registro, caminhos_sobre_1, caminhos_sobre_2
urlpatterns = [
    path('', index),
    path('alimento_em_rede/', caminhos_home_1),
    path('nossos_projetos/', caminhos_home_2),
    path('quem_somos/', caminhos_sobre_1),
    path('como_funcionamos/', caminhos_sobre_2),
    path('login/', caminhos_login),
    path('registro/', caminhos_registro),
    path('perfil', caminhos_perfil),
]