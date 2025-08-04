from rest_framework import serializers
from .models import TattooArtist
from apps.genders.models import Gender
from apps.location.models import Pais, Estado, Cidade
from apps.tattoo_styles.models import TattooStyle
from apps.tattoo_techniques.models import TattooTechnique
from apps.tattoo_machine_types.models import TattooMachineType
from apps.tattoo_product_brands.models import TattooProductBrand
from apps.tattoo_body_parts.models import TattooBodyPart

class TattooArtistSerializer(serializers.ModelSerializer):
    gender_id = serializers.PrimaryKeyRelatedField(
        queryset=Gender.objects.all(), source="gender", write_only=True, allow_null=True, required=False
    )
    gender = serializers.StringRelatedField(read_only=True)

    paises_que_atende = serializers.PrimaryKeyRelatedField(many=True, queryset=Pais.objects.all(), required=False)
    estados_que_atende = serializers.PrimaryKeyRelatedField(many=True, queryset=Estado.objects.all(), required=False)
    cidades_que_atende = serializers.PrimaryKeyRelatedField(many=True, queryset=Cidade.objects.all(), required=False)

    styles = serializers.PrimaryKeyRelatedField(many=True, queryset=TattooStyle.objects.all(), required=False)
    favorite_styles = serializers.PrimaryKeyRelatedField(many=True, queryset=TattooStyle.objects.all(), required=False)
    techniques = serializers.PrimaryKeyRelatedField(many=True, queryset=TattooTechnique.objects.all(), required=False)
    machine_types = serializers.PrimaryKeyRelatedField(many=True, queryset=TattooMachineType.objects.all(), required=False)
    product_brands = serializers.PrimaryKeyRelatedField(many=True, queryset=TattooProductBrand.objects.all(), required=False)
    body_parts_not_tattooed = serializers.PrimaryKeyRelatedField(many=True, queryset=TattooBodyPart.objects.all(), required=False)

    class Meta:
        model = TattooArtist
        fields = "__all__"
        read_only_fields = ["id", "created_at", "updated_at", "user"]
