from django.urls import path
from . import views 


urlpatterns = [
    path("add/", views.create, name="criarMeta"),
    path("", views.listartudo, name="listarMeta"),
    path("editar/<int:id_meta>", views.editar, name="atualizarMeta"),
    path("deletar/<int:id_meta>", views.deletar, name="confirmarMeta"),
    path("deletar/confirmar/<int:id_meta>", views.confirmarExcluir, name="confirmarMeta"),
]
