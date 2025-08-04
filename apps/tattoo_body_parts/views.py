from rest_framework import viewsets, permissions

from apps.tattoo_body_parts.serializer import TattooBodyPartSerializer
from .models import TattooBodyPart

class TattooBodyPartViewSet(viewsets.ModelViewSet):
    queryset = TattooBodyPart.objects.all()
    serializer_class = TattooBodyPartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
