from django.db import models
from django.contrib.auth import get_user_model
from apps.genders.models import Gender
from apps.tattoo_machine_types.models import TattooMachineType
from apps.tattoo_product_brands.models import TattooProductBrand
from apps.tattoo_styles.models import TattooStyle
from apps.tattoo_techniques.models import TattooTechnique
from apps.tattoo_body_parts.models import TattooBodyPart
from datetime import date
from django.core.exceptions import ValidationError
from apps.location.models import Pais, Estado, Cidade  

User = get_user_model()


class TattooArtist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="tattoo_profile")

    full_name = models.CharField("Nome completo", max_length=255)
    artistic_name = models.CharField("Nome artístico", max_length=30, unique=True)
    gender = models.ForeignKey(
        Gender,
        on_delete=models.SET_NULL,
        verbose_name="Gênero",
        related_name="tattoo_artists",
        null=True,
        blank=True,
    )
    birth_date = models.DateField("Data de nascimento")
    started_year = models.PositiveIntegerField("Ano que começou a tatuar", blank=True, null=True)

    photo = models.ImageField(
        "Foto de perfil",
        upload_to="artist_photos/",
        blank=True,
        null=True
    )

    is_apprentice = models.BooleanField("Aprendiz ou Iniciante", default=False)
    only_women = models.BooleanField("Atende apenas mulheres", default=False)
    safe_space = models.BooleanField("Espaço seguro", default=False)
    tattoos_private_parts = models.BooleanField("Tatua partes íntimas", default=False)

    body_parts_not_tattooed = models.ManyToManyField(
        TattooBodyPart,
        verbose_name="Partes do corpo que não tatua",
        related_name="tattoo_artists",
        blank=True
    )

    uses_vegan_products = models.BooleanField("Utiliza produtos veganos", default=False)

    instagram = models.URLField("Instagram", blank=True, null=True)
    whatsapp = models.CharField("WhatsApp", max_length=20, blank=True, null=True)
    business_phone = models.CharField("Telefone comercial", max_length=20, blank=True, null=True)

    watermark_tag = models.ImageField(
        "Tag/marca d'água",
        upload_to="watermarks/",
        blank=True,
        null=True
    )

    styles = models.ManyToManyField(
        TattooStyle,
        verbose_name="Estilos",
        related_name="tattoo_artists",
        blank=True
    )

    favorite_styles = models.ManyToManyField(
        TattooStyle,
        verbose_name="Estilos preferidos",
        related_name="preferred_by_artists",
        blank=True
    )

    techniques = models.ManyToManyField(
        TattooTechnique,
        verbose_name="Técnicas",
        related_name="tattoo_artists",
        blank=True
    )

    machine_types = models.ManyToManyField(
        TattooMachineType,
        verbose_name="Tipos de máquina que utiliza",
        related_name="tattoo_artists",
        blank=True
    )

    product_brands = models.ManyToManyField(
        TattooProductBrand,
        verbose_name="Marcas de produtos utilizados",
        related_name="tattoo_artists",
        blank=True
    )

    atende_em_outros_paises = models.BooleanField("Atende em outros países", default=False)
    atende_em_outros_estados = models.BooleanField("Atende em outros estados", default=False)
    atende_em_outras_cidades = models.BooleanField("Atende em outras cidades", default=False)

    paises_que_atende = models.ManyToManyField(
        Pais,
        verbose_name="Países onde atende",
        related_name="tattoo_artists",
        blank=True
    )
    estados_que_atende = models.ManyToManyField(
        Estado,
        verbose_name="Estados onde atende",
        related_name="tattoo_artists",
        blank=True
    )
    cidades_que_atende = models.ManyToManyField(
        Cidade,
        verbose_name="Cidades onde atende",
        related_name="tattoo_artists",
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tatuador"
        verbose_name_plural = "Tatuadores"
        db_table = "tattoo_artist"

    def __str__(self):
        return self.artistic_name or self.full_name

    def get_age(self):
        today = date.today()
        return today.year - self.birth_date.year - (
            (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )

    def clean(self):
        if self.favorite_styles.count() > 3:
            raise ValidationError("Você pode selecionar no máximo 3 estilos preferidos.")

    @property
    def stars_count(self):
        return self.favorited_by.count()
