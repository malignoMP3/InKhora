from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TattooMachineTypeViewSet

router = DefaultRouter()
router.register(r'', TattooMachineTypeViewSet, basename='tattoo-machine-types')

urlpatterns = [
    path('', include(router.urls)),
]
