from rest_framework import serializers
from .models import CameraImage
from .models import Camera


class CameraImagesSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = CameraImage
        fields = ['taken_at', 'image_url']

    def get_image_url(self, image):
        if image.image:
            return image.image.url


class CameraListSerializer(serializers.SerializerMethodField):
    class Meta:
        model = Camera
        fields = ['ip_address', 'name', 'registered_at']
