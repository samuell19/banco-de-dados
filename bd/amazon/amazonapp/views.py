from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Endereco, FormaPagamento, Vendedor, Perfil, Item, Pedido, PedidoItem
from .serializers import ClienteSerializer, EnderecoSerializer, FormaPagamentoSerializer, VendedorSerializer, PerfilSerializer, ItemSerializer, PedidoSerializer, PedidoItemSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer 

    @action(detail=False, methods=['get'])
    def clientes_sem_pedido(self, request):
        clientes_sem_pedido = self.queryset.exclude(pedido__isnull=False)
        serializer = ClienteSerializer(clientes_sem_pedido, many=True)
        return Response(serializer.data)


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

    @action(detail=False, methods=['get'])
    def estoque_baixo(self, request):
        baixo_estoque = self.queryset.filter(estoque__lt=10)
        serializer= ItemSerializer(baixo_estoque, many=True)
        return Response(serializer.data)

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    @action(detail=False, methods=['get'])
    def cliente_status(self, request):
        cliente_id=request.query_params.get('cliente_id')
        status=request.query_params.get('status', None)
        if cliente_id and status:
            pedidos = self.queryset.filter(cliente_id=cliente_id, status=status)
        else:
            pedidos = self.queryset.all()
        serializer = PedidoSerializer(pedidos, many=True)
        return Response(serializer.data)    

    @action(detail=True, methods=['get'])
    def entregue(self, request, pk=None):
        pedido = self.get_object()
        if pedido.status == 'Entregue':
            return Response({'status': 'Pedido já está entregue'})
        pedido.status = 'Entregue'
        pedido.save()
        serializer = PedidoSerializer(pedido)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def pedidos_entregues(self, request):
        pedidos_entregres= self.queryset.filter(status='Entregue')
        serializer = PedidoSerializer(pedidos_entregres, many=True)
        return Response(serializer.data)

class PedidoItemViewSet(viewsets.ModelViewSet):
    queryset = PedidoItem.objects.all()
    serializer_class = PedidoItemSerializer