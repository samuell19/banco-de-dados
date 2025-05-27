from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Usuario)
admin.site.register(Emprestimo)
admin.site.register(Reserva)
admin.site.register(Multa)
