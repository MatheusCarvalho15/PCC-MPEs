from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.create, name="criarVenda"),
    path("", views.listartudo, name="listarVenda"),
    path("editar/<int:id_venda>", views.editar, name="atualizarVenda"),
    path("deletar/<int:id_venda>", views.deletar, name="confirmarVenda"),
    path("deletar/confirmar/<int:id_venda>", views.confirmarExcluir, name="confirmarVenda"),
    path("detail/<int:id_venda>", views.detail, name="detail"),
    path("notaFiscal/<int:id_venda>", views.gerar_nota_fiscalVenda, name="notaFiscalVenda"),
]
