import csv
import re
from django.core.management.base import BaseCommand
from phones.models import Phone



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
        for phone in phones:
            recover = (re.sub(r'\s+', '-', (phone['name']), flags=re.UNICODE)).lower()
            tel = Phone(
                name=phone['name'],
                image=phone['image'],
                price=phone['price'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'],
                slug=recover
            )
            tel.save()
        return
