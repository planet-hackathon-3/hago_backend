import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class RandomCatImageAPI(APIView):
    def get(self, request):
        limit = 10
        if 'limit' in request.GET:
            limit = request.GET['limit']

        paylaod = {
            'limit': limit,
        }
        response = requests.get('https://api.thecatapi.com/v1/images/search', params=paylaod)
        return Response(data=response.json(), status=status.HTTP_200_OK)
