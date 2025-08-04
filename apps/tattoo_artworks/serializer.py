from rest_framework import serializers
from .models import TattooArtwork
from apps.tattoo_artist.models import TattooArtist

class TattooArtworkSerializer(serializers.ModelSerializer):
    tattoo_artist_id = serializers.PrimaryKeyRelatedField(
        queryset=TattooArtist.objects.all(), source="tattoo_artist", write_only=True
    )
    tattoo_artist = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TattooArtwork
        fields = [
            "id",
            "tattoo_artist",
            "tattoo_artist_id",
            "image",
            "type",
            "price",
            "description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
