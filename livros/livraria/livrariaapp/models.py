from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Editora(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.TextField()

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    ano_publicacao = models.PositiveIntegerField()
    genero = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    editora = models.ForeignKey(Editora, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.livro} emprestado para {self.usuario}"

class Reserva(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data_reserva = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} reservou {self.livro}"

class Multa(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    data_pagamento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Multa de {self.valor} para {self.usuario}"
