from rest_framework import serializers
from .models import TattooTechnique

class TattooTechniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattooTechnique
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
