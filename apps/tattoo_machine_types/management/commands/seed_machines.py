from django.core.management.base import BaseCommand
from apps.tattoo_machine_types.models import TattooMachineType


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        items = ["Bobina", "Rotativa", "Pen"]
        for name in items:
            TattooMachineType.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS("Tipos de máquina criados com sucesso."))
