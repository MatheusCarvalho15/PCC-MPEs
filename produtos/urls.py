from django.urls import path
from . import views


urlpatterns = [
    path("add/", views.criarProduto, name="criarProduto"),
    path("", views.listarProduto, name="listarProduto"),
    path("editar/<int:id_produto>", views.editar, name="atualizarProduto"),
    path("deletar/<int:id_produto>", views.deletar, name="confirmarProduto"),
    path("deletar/confirmar/<int:id_produto>", views.confirmarExcluir, name="confirmarProduto"),
]
