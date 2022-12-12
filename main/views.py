from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Camera, CameraImage
from .serializers import CameraListSerializer, CameraImagesSerializer


def homepage(request):
    cameras = Camera.objects.all()
    division_1 = cameras[:3]
    division_2 = cameras[3:]
    context = {"camera_row_1": division_1, "camera_row_2": division_2}
    return render(request, "index.html", context=context)


class CameraListAPIView(APIView):
    def get(self, request):
        cameras = Camera.objects.all()
        data = CameraListSerializer(cameras, many=True).data
        return Response(data=data)


class CameraImagesListAPIView(APIView):
    def get(self, request):
        camera_id = request.GET.get("camera_id")
        if camera_id:
            camera = Camera.objects.filter(id=camera_id).first()
            if camera:
                images = camera.cameraimage_set.all()
                data = CameraImagesSerializer(images, many=True).data
                return Response(data=data)
            return Response(data={"error": "Specified camera not found"}, status=400)
        return Response(data={"error": "invalid request"}, status=400)


def post_camera_image(request):
    print("hi")
    return JsonResponse(data={"message": "Saved successfully"}, status=200)
