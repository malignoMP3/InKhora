from django.db import models

class TattooBodyPart(models.Model):
    name = models.CharField("Parte do corpo", max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Parte do Corpo"
        verbose_name_plural = "Partes do Corpo"
        db_table = "tattoo_body_parts"

    def __str__(self):
        return self.name
