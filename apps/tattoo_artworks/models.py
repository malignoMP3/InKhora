from django.db import models
from apps.tattoo_artist.models import TattooArtist

class TattooArtwork(models.Model):
    class ArtworkType(models.TextChoices):
        PORTFOLIO = 'portfolio', "Portfólio"
        AVAILABLE = 'available', "Arte Disponível"
        INTERESTED = 'interested', "Deseja Tatuar"

    tattoo_artist = models.ForeignKey(
        TattooArtist,
        on_delete=models.CASCADE,
        related_name="artworks"
    )
    image = models.ImageField("Imagem da Arte", upload_to="artworks/")
    type = models.CharField(
        "Tipo da Arte",
        max_length=20,
        choices=ArtworkType.choices
    )
    price = models.DecimalField("Preço (opcional)", max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField("Descrição (opcional)", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Arte de Tatuagem"
        verbose_name_plural = "Artes de Tatuagem"
        db_table = "tattoo_artworks"

    def __str__(self):
        return f"{self.tattoo_artist.artistic_name} - {self.get_type_display()}"
