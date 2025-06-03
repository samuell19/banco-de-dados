from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from amazonapp import views

router = DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)
router.register(r'endereco', views.EnderecoViewSet)
router.register(r'forma_pagamento', views.FormaPagamentoViewSet)
router.register(r'vendedor', views.VendedorViewSet)
router.register(r'perfil', views.PerfilViewSet)
router.register(r'item', views.ItemViewSet)
router.register(r'pedido', views.PedidoViewSet)
router.register(r'item_pedido', views.PedidoItemViewSet)

urlpatterns = [
    path('amazon_api/', include(router.urls)),
]