from django.db import models

class Gender(models.Model):
    nome = models.CharField("Identidade de Gênero", max_length=100, unique=True)

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"
        db_table = "gender"

    def __str__(self):
        return self.nome