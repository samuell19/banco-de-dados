from reservaapp.models import Cliente, Endereco, FormaPagamento, Vendedor, Perfil, Item, Pedido, PedidoItem
from django.utils import timezone
from datetime import timedelta, date

# Criando Clientes
cliente1 = Cliente.objects.create(nome='João Silva', email='joao@email.com', telefone='11999999999')
cliente2 = Cliente.objects.create(nome='Maria Souza', email='maria@email.com', telefone='11888888888')

# Criando Endereços
endereco1 = Endereco.objects.create(cliente=cliente1, rua='Rua A', numero='123', bairro='Centro', cidade='SP', estado='SP', cep='01000-000')
endereco2 = Endereco.objects.create(cliente=cliente2, rua='Rua B', numero='456', bairro='Bairro B', cidade='RJ', estado='RJ', cep='20000-000')

# Formas de Pagamento
pix = FormaPagamento.objects.create(nome='Pix', descricao='Pagamento instantâneo', taxa=0.00)
boleto = FormaPagamento.objects.create(nome='Boleto', descricao='Pagamento em boleto', taxa=2.50)

# Vendedores
vendedor1 = Vendedor.objects.create(nome='Carlos Lima', email='carlos@email.com', telefone='11777777777')

# Perfis
perfil1 = Perfil.objects.create(cliente=cliente1, foto='fotos/semfoto.png', data_nascimento=date(1990, 5, 10), genero='M', cpf='123.456.789-00', tipo='F')
perfil2 = Perfil.objects.create(cliente=cliente2, foto='fotos/semfoto.png', data_nascimento=date(1985, 8, 20), genero='F', cpf='987.654.321-00', tipo='F')

# Itens
item1 = Item.objects.create(nome='Camiseta', descricao='Camiseta branca tamanho M', preco=49.90, estoque=100)
item2 = Item.objects.create(nome='Calça Jeans', descricao='Calça azul tamanho 42', preco=89.90, estoque=50)

# Pedidos
pedido1 = Pedido.objects.create(
    cliente=cliente1,
    vendedor=vendedor1,
    endereco_entrega=endereco1,
    forma_pagamento=pix,
    data_entrega=timezone.now() + timedelta(days=5)
)

pedido2 = Pedido.objects.create(
    cliente=cliente2,
    vendedor=vendedor1,
    endereco_entrega=endereco2,
    forma_pagamento=boleto,
    data_entrega=timezone.now() + timedelta(days=3)
)

# PedidoItem (relacionamento intermediário)
PedidoItem.objects.create(pedido=pedido1, item=item1, quantidade=2, preco_unitario=item1.preco, subtotal=2 * item1.preco)
PedidoItem.objects.create(pedido=pedido1, item=item2, quantidade=1, preco_unitario=item2.preco, subtotal=1 * item2.preco)
PedidoItem.objects.create(pedido=pedido2, item=item2, quantidade=3, preco_unitario=item2.preco, subtotal=3 * item2.preco)
