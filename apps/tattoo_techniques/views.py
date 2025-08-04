from rest_framework import viewsets, permissions
from apps.tattoo_techniques.serializer import TattooTechniqueSerializer
from .models import TattooTechnique

class TattooTechniqueViewSet(viewsets.ModelViewSet):
    queryset = TattooTechnique.objects.all()
    serializer_class = TattooTechniqueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
