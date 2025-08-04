from django.core.management.base import BaseCommand

from django.db import transaction

from apps.location.models import Cidade, Estado, Pais

class Command(BaseCommand):
    help = "Popula Brasil com os estados SP e RJ e algumas cidades"

    def handle(self, *args, **kwargs):
        self.stdout.write("🚀 Iniciando seed de localidades brasileiras...")

        with transaction.atomic():
            brasil, _ = Pais.objects.get_or_create(nome="Brasil", sigla="BR")
            self.stdout.write(self.style.SUCCESS(f"✅ País criado: {brasil.nome} ({brasil.sigla})"))

         
            sp, _ = Estado.objects.get_or_create(nome="São Paulo", sigla="SP", pais=brasil)
            self.stdout.write(self.style.SUCCESS(f"📍 Estado criado: {sp.nome}"))
            cidades_sp = ["Hortolândia", "Campinas", "Sumaré", "São Paulo"]
            for nome_cidade in cidades_sp:
                Cidade.objects.get_or_create(nome=nome_cidade, estado=sp)
            self.stdout.write(f"🏙️  Cidades de SP adicionadas: {', '.join(cidades_sp)}")

            
            rj, _ = Estado.objects.get_or_create(nome="Rio de Janeiro", sigla="RJ", pais=brasil)
            self.stdout.write(self.style.SUCCESS(f"📍 Estado criado: {rj.nome}"))
            cidades_rj = ["Rio de Janeiro", "Niterói", "Petrópolis"]
            for nome_cidade in cidades_rj:
                Cidade.objects.get_or_create(nome=nome_cidade, estado=rj)
            self.stdout.write(f"🏙️  Cidades do RJ adicionadas: {', '.join(cidades_rj)}")

        self.stdout.write(self.style.SUCCESS("🌍 Seed finalizada com sucesso."))
