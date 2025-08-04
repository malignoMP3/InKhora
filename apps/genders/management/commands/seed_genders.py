from django.core.management.base import BaseCommand
from apps.genders.models import Gender

class Command(BaseCommand):
    help = "Popula a tabela de gêneros com valores padrão."

    GENDER_LIST = [
        "Mulher cis",
        "Homem cis",
        "Mulher trans",
        "Homem trans",
        "Não-binário",
        "Prefere não informar",
        "Outro",
    ]

    def handle(self, *args, **kwargs):
        count = 0
        for nome in self.GENDER_LIST:
            gender, created = Gender.objects.get_or_create(nome=nome)
            if created:
                count += 1
                self.stdout.write(self.style.SUCCESS(f"✓ Gênero adicionado: {nome}"))
            else:
                self.stdout.write(self.style.WARNING(f"- Gênero já existe: {nome}"))

        self.stdout.write(self.style.SUCCESS(f"✅ Seed finalizada. {count} novos registros adicionados."))
