from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TattooProductBrandViewSet

router = DefaultRouter()
router.register(r'', TattooProductBrandViewSet, basename='tattoo-product-brands')

urlpatterns = [
    path('', include(router.urls)),
]
