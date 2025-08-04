from django.db import models
from django.conf import settings
from apps.tattoo_artist.models import TattooArtist

class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorites"
    )
    tattoo_artist = models.ForeignKey(
        TattooArtist,
        on_delete=models.CASCADE,
        related_name="favorited_by"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'tattoo_artist') 
        verbose_name = "Favorito"
        verbose_name_plural = "Favoritos"
        db_table = "favorites"

    def __str__(self):
        return f"{self.user.email} ⭐ {self.tattoo_artist.artistic_name}"
