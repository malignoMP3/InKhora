from rest_framework import viewsets, permissions
from apps.tattoo_machine_types.serializer import TattooMachineTypeSerializer
from .models import TattooMachineType

class TattooMachineTypeViewSet(viewsets.ModelViewSet):
    queryset = TattooMachineType.objects.all()
    serializer_class = TattooMachineTypeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
