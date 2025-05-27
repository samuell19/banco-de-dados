from datetime import date, timedelta
from random import choice, randint
from livrariaapp.models import Autor, Livro, Usuario, Emprestimo, Reserva, Multa, Categoria, Editora

# Criar categorias
cat_ficcao = Categoria.objects.create(nome="Ficção", descricao="Livros de ficção")
cat_nao_ficcao = Categoria.objects.create(nome="Não-ficção", descricao="Livros baseados em fatos reais")

# Criar editoras
editora1 = Editora.objects.create(nome="Editora Globo", endereco="Rua A, 123")
editora2 = Editora.objects.create(nome="Companhia das Letras", endereco="Av. B, 456")

# Criar autores
autor1 = Autor.objects.create(nome="Machado de Assis", data_nascimento="1839-06-21", nacionalidade="Brasileiro")
autor2 = Autor.objects.create(nome="George Orwell", data_nascimento="1903-06-25", nacionalidade="Britânico")

# Criar livros
livro1 = Livro.objects.create(
    titulo="Dom Casmurro", autor=autor1, ano_publicacao=1899,
    genero="Romance", categoria=cat_ficcao, editora=editora1
)
livro2 = Livro.objects.create(
    titulo="1984", autor=autor2, ano_publicacao=1949,
    genero="Distopia", categoria=cat_ficcao, editora=editora2
)

# Criar usuários
usuario1 = Usuario.objects.create(nome="João da Silva", email="joao@example.com", data_registro=date.today())
usuario2 = Usuario.objects.create(nome="Maria Oliveira", email="maria@example.com", data_registro=date.today())

# Criar empréstimos
Emprestimo.objects.create(livro=livro1, usuario=usuario1, data_emprestimo=date.today() - timedelta(days=7))
Emprestimo.objects.create(livro=livro2, usuario=usuario2, data_emprestimo=date.today() - timedelta(days=3))

# Criar reservas
Reserva.objects.create(livro=livro1, usuario=usuario2, data_reserva=date.today())
Reserva.objects.create(livro=livro2, usuario=usuario1, data_reserva=date.today() - timedelta(days=1))

# Criar multas
Multa.objects.create(usuario=usuario1, valor=15.00, data_pagamento=date.today() - timedelta(days=2))
Multa.objects.create(usuario=usuario2, valor=10.00, data_pagamento=date.today())

print("Banco de dados populado com sucesso!")
