from django.db import models

class TattooTechnique(models.Model):
    name = models.CharField("Nome da técnica", max_length=100, unique=True)
    description = models.TextField("Descrição da técnica", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Técnica de Tatuagem"
        verbose_name_plural = "Técnicas de Tatuagem"
        db_table = "tattoo_techniques"

    def __str__(self):
        return self.name
