from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.create, name="criar"),
    path("", views.listartudo, name="listar"),
    path("editar/<int:id_despesa>", views.editar, name="atualizar"),
    path("deletar/<int:id_despesa>", views.deletar, name="confirmar"),
    path("deletar/confirmar/<int:id_despesa>", views.confirmarExcluir, name="confirmar"),
    path("detail/<int:id_despesa>", views.detail, name="detail"),
    
]

