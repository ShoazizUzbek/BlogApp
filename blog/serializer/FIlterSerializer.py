from rest_framework import serializers


class FilterSerializer(serializers.Serializer):

    added_at = serializers.DateField(required=False)
    tags = serializers.ListField(child=serializers.IntegerField(),required=False)