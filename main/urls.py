from django.urls import path
from .views import homepage, CameraListAPIView, CameraImagesListAPIView, post_camera_image

urlpatterns = [
    path("", homepage, name="homepage"),
    path("cameras", CameraListAPIView.as_view(), name="camera-list"),
    path("cameras/<int:camera_id>/images",
         CameraImagesListAPIView.as_view(), name="camera-images"),
    path("cameras/save-image",
         post_camera_image, name="save-image")
]
