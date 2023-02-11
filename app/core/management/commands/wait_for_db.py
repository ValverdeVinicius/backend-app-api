"""
Comando do Django para aguardar o banco de dados estar disponível
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Comando Django para esperar pelo database"""

    def handle(self, *args, **options):
        """Entrypoint para o comando"""
        self.stdout.write('Esperando pelo Database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Databse indisponível, espere 1 seg...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database disponível!'))
