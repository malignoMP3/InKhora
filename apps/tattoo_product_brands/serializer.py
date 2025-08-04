from rest_framework import serializers
from .models import TattooProductBrand

class TattooProductBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattooProductBrand
        fields = ['id', 'name', 'description', 'logo', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
