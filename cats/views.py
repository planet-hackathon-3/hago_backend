import random

from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cats.models import CatImage
from cats.serializers import CatImageSerializer


class RandomCatImageAPI(APIView):
    def get(self, request):
        limit = request.GET.get('limit', 30)

        cached_list = cache.get('random_cat_image_list')
        if not cached_list:
            cat_image_id_list = list(CatImage.objects.values_list('id', flat=True))
            random_image_id_list = random.sample(cat_image_id_list, limit)
            cached_list = CatImage.objects.filter(id__in=random_image_id_list)

        serializer = CatImageSerializer(cached_list, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
