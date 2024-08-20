
from django.contrib import admin
from django.contrib.auth import urls
from django.urls import include, path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('accounts/', include("accounts.urls")),
    path('accounts/', include(urls)),
    path("despesas/", include("despesas.urls")),
    path("home/", views.home, name="home"),
    path("produtos/", include("produtos.urls")),
    path("compra/", include("compra.urls")),
    path("meta/", include("metaLucro.urls")),
    path("venda/", include("venda.urls")),
    path("admin/", admin.site.urls),

]