from rest_framework import viewsets, permissions
from apps.tattoo_product_brands.serializer import TattooProductBrandSerializer
from .models import TattooProductBrand

class TattooProductBrandViewSet(viewsets.ModelViewSet):
    queryset = TattooProductBrand.objects.all()
    serializer_class = TattooProductBrandSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
