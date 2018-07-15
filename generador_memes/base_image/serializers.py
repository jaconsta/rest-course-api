from rest_framework import serializers

from .models import Image


class ImageSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=150)

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
