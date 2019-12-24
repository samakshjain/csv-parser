import csv

from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError

from main.models import Data


class Command(BaseCommand):
    help = 'Populates the data from the given CSV'

    def add_arguments(self, parser):
        parser.add_argument('file_path')

    def handle(self, *args, **options):
        try:
            with open('data.csv', mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter='|', fieldnames=[
                    'reference_id', 'timestamp', 'handle', 'tweet'
                ])
                for row in csv_reader:
                    Data.objects.create(**row)
        except IntegrityError:
            raise CommandError("Cannot insert data, probably unsupported data")
