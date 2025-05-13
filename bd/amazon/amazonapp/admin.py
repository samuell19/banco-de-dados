from django.contrib import admin
from .models import Cliente, Endereco, FormaPagamento, Vendedor, Perfil, Item, Pedido, PedidoItem

admin.site.register(Cliente)
admin.site.register(Endereco)
admin.site.register(FormaPagamento)
admin.site.register(Vendedor)
admin.site.register(Perfil)
admin.site.register(Item)
admin.site.register(Pedido)
admin.site.register(PedidoItem)