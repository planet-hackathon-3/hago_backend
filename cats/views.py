import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class RandomCatImageAPI(APIView):
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "3f086b82-2020-48f7-938b-f30d824fa055",
    }

    def get(self, request):
        limit = 10
        if 'limit' in request.GET:
            limit = request.GET['limit']

        paylaod = {
            'limit': limit,
        }
        response = requests.get('https://api.thecatapi.com/v1/images/search', params=paylaod)
        return Response(data=response.json(), status=status.HTTP_200_OK)
