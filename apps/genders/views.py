from rest_framework import viewsets
from apps.genders.serializer import GenderSerializer
from .models import Gender
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
