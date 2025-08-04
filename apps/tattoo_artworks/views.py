from rest_framework import viewsets, permissions

from apps.tattoo_artworks.serializer import TattooArtworkSerializer
from .models import TattooArtwork

class TattooArtworkViewSet(viewsets.ModelViewSet):
    queryset = TattooArtwork.objects.all()
    serializer_class = TattooArtworkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()
