from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.parsers import JSONParser, MultiPartParser

from .models import Image
from .forms import ImageUploadForm
from .serializers import ImageSerializer, ImageUploadSerializer


class FileUploadView(viewsets.GenericViewSet):
    parser_classes = (MultiPartParser, )
    serializer_class = ImageUploadSerializer

    def create(self, request):
        form = ImageUploadForm(request.POST, request.FILES)
        if not form.is_valid():
            return JsonResponse({'error': 'Bad image form'})
        form.save()
        response_body = ImageSerializer(form.instance).data
        return JsonResponse(response_body, status=201)


class ImageViewSet(viewsets.GenericViewSet):
    """
    The images that will be used as background for the memes.

    list:
    Return all base images, currently not sorted.
    """
    parser_classes = (JSONParser, )
    serializer_class = ImageSerializer

    def list(self, request):
        images = Image.objects.all()
        images_serialized = ImageSerializer(images, many=True)
        return JsonResponse(images_serialized.data, safe=False)

    def retrieve(self, request, pk=None):
        try:
            image = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return JsonResponse({"error": "Image does not exist."}, status=404)
        image_serialize = ImageSerializer(image)
        return JsonResponse(image_serialize.data)

    def update(self, request, pk=None):
        try:
            image = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return JsonResponse({"error": "Image does not exist."}, status=404)
        update_data = JSONParser().parse(request)
        data_serialized = ImageSerializer(image, data=update_data)
        if not data_serialized.is_valid():
            return JsonResponse(data_serialized.errors, status=400)
        data_serialized.save()
        return JsonResponse(data_serialized.data)

    def destroy(self, request, pk=None):
        try:
            image = Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            return JsonResponse({"error": "Image does not exist."}, status=404)
        image.delete()
        return JsonResponse({'message': 'deleted'}, status=204)
