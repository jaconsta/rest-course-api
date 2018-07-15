from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt


def fetch_images(request):
    """
    Manual implementation of the endpoint
    :param request:
    :return: [{"name": "first", "file": "white.png"}, {"name": "second", "file": "one.png"}]
    """
    images = [
        {
            'name': 'first',
            'file': 'white.png'
        }, {
            'name': 'second',
            'file': 'one.png'
        }
    ]
    return JsonResponse(images, safe=False)


@csrf_exempt
def add_images(request):
    """
    Manual implementation of the endpoint
    :param request:
    :return:
    """
    if request.method != 'POST':
        return JsonResponse({'message': 'Method not allowed'}, status=403)

    image = {
        'id': 1,
        'name': request.POST.get('name'),
        'file': '/static/test_files/{filename}'.format(filename=request.FILES.get('file').name)
    }

    return JsonResponse(image, safe=False, status=201)
