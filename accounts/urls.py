
from accounts.views import register, listarUsuarios, editarFunção, deletarUsuario, listarDados, editarDados
from django.urls import path 


urlpatterns = [
    #cadastroForaDoSistema
    path('register/', register, name='register'),
    path('Usuarios/', listarUsuarios, name='listarUsuarios'),
    path('listarDados/', listarDados, name='listarDados'),
    path('editarUsuario/<int:id_user>', editarFunção, name='editarUsuario'),
    path('editarDados/<int:id_user>', editarDados, name='editarDados'),
    path('deletarUsuario/<int:id_user>', deletarUsuario, name='deletarUsuario')

]