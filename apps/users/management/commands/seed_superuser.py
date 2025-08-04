from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Cria o superusuário Maligno, se não existir"

    def handle(self, *args, **kwargs):
        User = get_user_model()
        if not User.objects.filter(username="Maligno").exists():
            User.objects.create_superuser(
                username="Maligno",
                email="maligno@inkhora.com",
                password="Area72123-",
                tipo_de_usuario=User.UserType.ROOT
            )
            self.stdout.write(self.style.SUCCESS("Superusuário Maligno criado com sucesso."))
        else:
            self.stdout.write(self.style.WARNING("Superusuário Maligno já existe."))