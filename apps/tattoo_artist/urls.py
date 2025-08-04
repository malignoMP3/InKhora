from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TattooArtistViewSet

router = DefaultRouter()
router.register(r'', TattooArtistViewSet, basename='tattoo-artists')

urlpatterns = [
    path('', include(router.urls)),
]
