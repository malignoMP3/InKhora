from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TattooTechniqueViewSet

router = DefaultRouter()
router.register(r'', TattooTechniqueViewSet, basename='tattoo-techniques')

urlpatterns = [
    path('', include(router.urls)),
]
