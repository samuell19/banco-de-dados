from rest_framework import serializers
from .models import Cliente, Endereco, FormaPagamento, Vendedor, Perfil, Item, Pedido, PedidoItem

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__' 

class  EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'     

class FormaPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPagamento
        fields = '__all__'


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class PedidoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoItem
        fields = '__all__'                