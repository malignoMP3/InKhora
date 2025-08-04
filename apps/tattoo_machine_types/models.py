from django.db import models

class TattooMachineType(models.Model):
    name = models.CharField("Tipo de máquina", max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tipo de Máquina"
        verbose_name_plural = "Tipos de Máquina"
        db_table = "tattoo_machine_types"

    def __str__(self):
        return self.name
