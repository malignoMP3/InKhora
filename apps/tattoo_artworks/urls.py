from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TattooArtworkViewSet

router = DefaultRouter()
router.register(r'', TattooArtworkViewSet, basename='tattoo-artworks')

urlpatterns = [
    path('', include(router.urls)),
]
