import random

from django.core.cache import cache
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from cats.models import CatImage, Tip
from cats.serializers import CatImageSerializer, TipSerializer


class RandomCatImageAPI(APIView):
    def get(self, request):
        limit = int(request.GET.get('limit', 30))

        cached_list = cache.get('random_cat_image_list')
        if not cached_list:
            # caching 안된 경우
            cat_image_id_list = list(CatImage.objects.values_list('id', flat=True))
            random_image_id_list = random.sample(cat_image_id_list, limit)
            cached_list = CatImage.objects.filter(id__in=random_image_id_list)
        else:
            # caching 된 경우
            cached_list = cached_list[:limit]

        serializer = CatImageSerializer(cached_list, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CatImageDetailAPI(APIView):
    def get(self, request, image_id):
        cat_image = get_object_or_404(CatImage, id=image_id)
        serializer = CatImageSerializer(cat_image)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class LikeCatImage(APIView):
    def post(self, request, image_id):
        try:
            cat_image = get_object_or_404(CatImage, id=image_id)
            cat_image.like_count += 1
            cat_image.save(update_fields=['like_count'])
        except Exception as e:
            return Response(data={'success': False}, status=status.HTTP_200_OK)
        return Response(data={'success': True}, status=status.HTTP_200_OK)


class RandomTipAPI(APIView):
    def get(self, request):
        random_tip = Tip.objects.order_by('?').first()
        serializer = TipSerializer(random_tip)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
