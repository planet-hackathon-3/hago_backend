from rest_framework import serializers


class CatImageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    id_for_api = serializers.CharField()
    url = serializers.URLField()
    like_count = serializers.IntegerField()
