from rest_framework import permissions

class IsGerente(permissions.BasePermission):
    """
    Permissão personalizada para permitir apenas usuários do tipo 'gerente'.
    """
    message = 'Apenas gerentes podem realizar esta ação.'

    def has_permission(self, request, view):  
        if not request.user.is_authenticated:
            return False
        return request.user.tipo == 'gerente'

