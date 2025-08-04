from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TattooBodyPartViewSet

router = DefaultRouter()
router.register(r'', TattooBodyPartViewSet, basename='tattoo-body-parts')

urlpatterns = [
    path('', include(router.urls)),
]
