from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router= DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditoraViewSet)
router.register(r'autores', AutorViewSet)
router.register(r'livros', LivroViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'emprestimos', EmprestimoViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'multas', MultaViewSet)
urlpatterns = [
    path('', include(router.urls)),
]