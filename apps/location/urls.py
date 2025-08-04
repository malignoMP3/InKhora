from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaisViewSet, EstadoViewSet, CidadeViewSet

router = DefaultRouter()
router.register(r'paises', PaisViewSet, basename='pais')
router.register(r'estados', EstadoViewSet, basename='estado')
router.register(r'cidades', CidadeViewSet, basename='cidade')

urlpatterns = [
    path('', include(router.urls)),
]
