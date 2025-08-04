from rest_framework import serializers
from .models import TattooBodyPart

class TattooBodyPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattooBodyPart
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
