from django.urls import path
from caminhos.views import index, caminhos_perfil, caminhos_login, caminhos_registro, caminhos_sobre_1
urlpatterns = [
    path('', index, name='levar_menu'),
    path('quem_somos/', caminhos_sobre_1, name = 'levar_sobre'),
    path('login/', caminhos_login, name= 'levar_login'),
    path('registro/', caminhos_registro, name = 'listagem_usuarios'),
    path('perfil/', caminhos_perfil, name= 'levar_perfil'), 
]