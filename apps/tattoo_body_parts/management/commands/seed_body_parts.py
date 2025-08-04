from django.core.management.base import BaseCommand
from apps.tattoo_body_parts.models import TattooBodyPart

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        parts = ["Mãos", "Pés", "Cabeça", "Rosto", "Pescoço", "Costelas", "Região íntima"]
        for name in parts:
            TattooBodyPart.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS("Partes do corpo criadas com sucesso."))
