from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import Camera

cameras = [
    {"name": "Camera 1"},
    {"name": "Camera 2"},
    {"name": "Camera 3"},
    {"name": "Camera 4"},
    {"name": "Camera 5"},
]


class Command(BaseCommand):
    def handle(self, *args, **options):
        for camera in cameras:
            Camera.objects.create(name=camera.get("name"))
        admin = User.objects.filter(username="admin").first()
        if not admin:
            user = User.objects.create(
                username="admin",
                email="admin@admin.admin",
                is_staff=True,
                is_superuser=True
            )
            user.set_password("password")
            user.save()
