from rest_framework import serializers
from .models import TattooMachineType

class TattooMachineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TattooMachineType
        fields = ['id', 'name', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
