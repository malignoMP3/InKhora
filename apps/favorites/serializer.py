from rest_framework import serializers
from .models import Favorite
from apps.tattoo_artist.models import TattooArtist

class FavoriteSerializer(serializers.ModelSerializer):
    tattoo_artist_id = serializers.PrimaryKeyRelatedField(
        queryset=TattooArtist.objects.all(),
        source='tattoo_artist',
        write_only=True
    )

    tattoo_artist_name = serializers.CharField(source='tattoo_artist.artistic_name', read_only=True)
    tattoo_artist_id_read = serializers.IntegerField(source='tattoo_artist.id', read_only=True)

    class Meta:
        model = Favorite
        fields = ['id', 'tattoo_artist_id', 'tattoo_artist_id_read', 'tattoo_artist_name', 'created_at']
        read_only_fields = ['id', 'created_at']
