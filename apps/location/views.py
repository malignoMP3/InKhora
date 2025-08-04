from rest_framework import viewsets
from .models import Pais, Estado, Cidade
from .serializers import PaisSerializer, EstadoSerializer, CidadeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CidadeViewSet(viewsets.ModelViewSet):
    queryset = Cidade.objects.all()
    serializer_class = CidadeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
