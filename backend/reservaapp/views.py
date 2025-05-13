from reservaapp.serializers import CustomUserSerializer, EspacoEsportivoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView
from .models import CustomUser, EspacoEsportivo
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from .permissions import IsGerente


class CustomUserCreateView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]

    
class EspacoEsportivo(viewsets.ModelViewSet): #fazer com create depois
    queryset = EspacoEsportivo.objects.all()
    serializer_class = EspacoEsportivoSerializer
    permission_classes = [IsGerente]

    def perform_create(self, serializer):
        serializer.save(gerente=self.request.user)
 