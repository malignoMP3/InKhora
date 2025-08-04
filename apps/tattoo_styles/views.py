from rest_framework import viewsets, permissions

from apps.tattoo_styles.serializer import TattooStyleSerializer
from .models import TattooStyle


class TattooStyleViewSet(viewsets.ModelViewSet):
    queryset = TattooStyle.objects.all()
    serializer_class = TattooStyleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
