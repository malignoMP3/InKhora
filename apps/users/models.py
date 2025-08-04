from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class UserType(models.TextChoices):
        ROOT = "Maligno", "Chefão"
        TATUADOR = "tatuador", "Tatuador"
        USUARIO = "usuario", "Usuário"

    email = models.EmailField(unique=True)
    phone = models.CharField("Telefone", max_length=20, unique=True, null=True, blank=True)
    tipo_de_usuario = models.CharField(
        "Tipo de Usuário",
        max_length=20,
        choices=UserType.choices,
        default=UserType.USUARIO
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
