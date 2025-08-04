from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GenderViewSet

router = DefaultRouter()
router.register(r'genders', GenderViewSet, basename='gender')

urlpatterns = [
    path('', include(router.urls)),
]
