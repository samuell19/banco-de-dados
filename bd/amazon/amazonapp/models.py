from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f'{self.nome} - {self.email} - {self.telefone}'



class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2) 
    cep = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.rua}, {self.numero} - {self.bairro}, {self.cidade}/{self.estado} - {self.cep}'



class FormaPagamento(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=100)
    taxa = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f'{self.nome} - {self.descricao} - {self.taxa}'        
  

class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nome} - {self.email} - {self.telefone}'


class Perfil(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos/')
    data_nascimento = models.DateField()
    genero = models.CharField(max_length=1, choices=(('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')))
    cpf = models.CharField(max_length=14)
    tipo = models.CharField(max_length=1, choices=(('F', 'Física'), ('J', 'Jurídica')))

    def __str__(self):
        return f'{self.cliente.nome} - {self.genero} - {self.data_nascimento}'


class Item (models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.IntegerField()
    
    def __str__(self):
        return f'{self.nome} - {self.descricao} - R$ {self.preco} - Estoque: {self.estoque}'


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    endereco_entrega = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    itens = models.ManyToManyField(Item, through='PedidoItem')
    forma_pagamento = models.ForeignKey(FormaPagamento, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateTimeField()
    
    def __str__(self): 
        return f'{self.cliente} - {self.vendedor} - {self.data_pedido}'                          

class PedidoItem(models.Model):

    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=8, decimal_places=2)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.pedido} - {self.item} - {self.quantidade} - R$ {self.subtotal}'
