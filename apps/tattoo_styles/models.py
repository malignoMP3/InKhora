from django.db import models

class TattooStyle(models.Model):
    name = models.CharField("Nome do estilo", max_length=100, unique=True)
    description = models.TextField("Descrição do estilo", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Estilo de Tatuagem"
        verbose_name_plural = "Estilos de Tatuagem"
        db_table = "tattoo_styles"

    def __str__(self):
        return self.name
