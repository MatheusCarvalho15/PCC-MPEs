from django.urls import path
from . import views


urlpatterns = [
    path("adicionar/", views.create, name="criarCompra"),
    path("", views.listartudo, name="listarCompra"),
    path("editar/<int:id_compra>", views.editar, name="atualizarCompra"),
    path("deletar/<int:id_compra>", views.deletar, name="confirmarCompra"),
    path("deletar/confirmar<int:id_compra>", views.confirmarExcluir, name="confirmarCompra"),
    path("notaFiscal/<int:id_compra>", views.gerar_nota_fiscalCompra, name="notaFiscalCompra")
    
]
