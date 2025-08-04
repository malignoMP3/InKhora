from rest_framework import viewsets, permissions

from apps.tattoo_artist.serializer import TattooArtistSerializer
from .models import TattooArtist

class TattooArtistViewSet(viewsets.ModelViewSet):
    queryset = TattooArtist.objects.all()
    serializer_class = TattooArtistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
