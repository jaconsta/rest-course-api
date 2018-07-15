from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Image
from base_image.serializers import ImageSerializer


@csrf_exempt
def image_list(request):
    if request.method == 'GET':
        images = Image.objects.all()
        images_serialized = ImageSerializer(images, many=True)
        return JsonResponse(images_serialized.data, safe=False)
    if request.method == 'POST':
        serialized_data = Image(name=request.POST['name'], file=request.FILES['file'])
        serialized_data.save()
        return JsonResponse(ImageSerializer(serialized_data).data, status=201)


@csrf_exempt
def image_detail(request, image_id):
    try:
        image = Image.objects.get(pk=image_id)
    except Image.DoesNotExist:
            return JsonResponse({'message': 'Image Not Found'}, status=404)

    if request.method == 'GET':
        image_serialize = ImageSerializer(image)
        return JsonResponse(image_serialize.data)

    if request.method == 'PUT':
        update_data = JSONParser().parse(request)
        data_serialized = ImageSerializer(image, data=update_data)
        if not data_serialized.is_valid():
            return JsonResponse(data_serialized.errors, status=400)
        data_serialized.save()
        return JsonResponse(data_serialized.data)

    if request.method == 'DELETE':
        image.delete()
        return JsonResponse({'message': 'deleted'}, status=204)
