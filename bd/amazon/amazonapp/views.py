from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Endereco, FormaPagamento, Vendedor, Perfil, Item, Pedido, PedidoItem
from .serializers import ClienteSerializer, EnderecoSerializer, FormaPagamentoSerializer, VendedorSerializer, PerfilSerializer, ItemSerializer, PedidoSerializer, PedidoItemSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer 


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class FormaPagamentoViewSet(viewsets.ModelViewSet):
    queryset = FormaPagamento.objects.all()
    serializer_class = FormaPagamentoSerializer

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoItemViewSet(viewsets.ModelViewSet):
    queryset = PedidoItem.objects.all()
    serializer_class = PedidoItemSerializer