from django.core.management.base import BaseCommand
from main.models import Camera


class Command(BaseCommand):
    def handle(self, *args, **options):
        Camera.objects.all().delete()
