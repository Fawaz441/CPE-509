from django.db import models
from django.utils import timezone


class Camera(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    registered_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name if self.name else str(self.id)

    @property
    def get_full_ip_address(self):
        if self.ip_address:
            return "http://"+self.ip_address


class CameraImage(models.Model):

    def get_camera_image_path(self, filename):
        now = timezone.now()
        camera_name = self.camera.name if self.camera else str(self.id)
        return f'{camera_name}/{now.year}-{now.month}-{now.date()}/{filename}'

    camera = models.ForeignKey(
        Camera, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to=get_camera_image_path)
    taken_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-taken_at']
