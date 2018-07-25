from rest_framework import serializers

from .models import Image


class ImageUploadSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    file = serializers.ImageField()


class ImageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)
    file = serializers.ImageField(read_only=True)

    model = Image

    def create(self, validated_data):
        """
        Add new data to our models.

        :param validated_data:
        :return:
        """
        return self.model.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update the model information.

        :param instance:
        :param validated_data:
        :return:
        """
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        return instance
