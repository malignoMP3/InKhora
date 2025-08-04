from rest_framework import serializers
from .models import Pais, Estado, Cidade

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['id', 'nome', 'sigla']

class EstadoSerializer(serializers.ModelSerializer):
    pais = PaisSerializer(read_only=True)
    pais_id = serializers.PrimaryKeyRelatedField(queryset=Pais.objects.all(), source='pais', write_only=True)

    class Meta:
        model = Estado
        fields = ['id', 'nome', 'sigla', 'pais', 'pais_id']

class CidadeSerializer(serializers.ModelSerializer):
    estado = EstadoSerializer(read_only=True)
    estado_id = serializers.PrimaryKeyRelatedField(queryset=Estado.objects.all(), source='estado', write_only=True)

    class Meta:
        model = Cidade
        fields = ['id', 'nome', 'estado', 'estado_id']
