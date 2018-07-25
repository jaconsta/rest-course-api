"""generador_memes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .openapi_config import schema_view
from base_image.views import ImageViewSet, FileUploadView

router = DefaultRouter()
router.register('base_images', ImageViewSet, base_name='base_images')
router.register('uploads/base_images', FileUploadView, base_name='upload_base__images')


urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/v1/', include(router.urls)),
    url(r'^api-doc/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    url(r'^api-doc/$', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
]
