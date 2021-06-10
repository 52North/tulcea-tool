
from rest_framework import serializers
from wq.db.patterns import serializers as patterns
from .models import Producer, Photo


class PhotoSerializer(patterns.AttachmentSerializer):
    class Meta(patterns.AttachmentSerializer.Meta):
        model = Photo
        exclude = ('producer',)
        object_field = 'producer'


class ProducerSerializer(patterns.AttachedModelSerializer):
    photos = PhotoSerializer(many=True, required=False)

    class Meta:
        model = Producer
        fields = "__all__"
