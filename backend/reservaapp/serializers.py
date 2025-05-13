from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import EspacoEsportivo, Recurso, Agenda


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'tipo', 'nome_completo', 'cpf', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user
    
class EspacoEsportivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspacoEsportivo
        exclude = ['gerente']