from django.db import models

class TattooProductBrand(models.Model):
    name = models.CharField("Nome da marca", max_length=100, unique=True)
    description = models.TextField("Descrição", blank=True, null=True)

    logo = models.ImageField(
        "Logo da marca",
        upload_to="brand_logos/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Marca de Produto"
        verbose_name_plural = "Marcas de Produtos"
        db_table = "tattoo_product_brands"

    def __str__(self):
        return self.name
