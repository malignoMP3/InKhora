from django.db import models


class Pais(models.Model):
    nome = models.CharField("Nome do país", max_length=100, unique=True)
    sigla = models.CharField("Sigla", max_length=5, unique=True)

    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
        db_table = "pais"

    def __str__(self):
        return f"{self.nome} ({self.sigla})"


class Estado(models.Model):
    nome = models.CharField("Nome do estado", max_length=100)
    sigla = models.CharField("Sigla do estado", max_length=5)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name="estados")

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        db_table = "estado"
        unique_together = ("sigla", "pais")

    def __str__(self):
        return f"{self.nome} ({self.sigla}) - {self.pais.sigla}"



class Cidade(models.Model):
    nome = models.CharField("Nome da cidade", max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="cidades")

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"
        db_table = "cidade"
        unique_together = ("nome", "estado")

    def __str__(self):
        return f"{self.nome} - {self.estado.nome} / {self.estado.pais.nome}"
