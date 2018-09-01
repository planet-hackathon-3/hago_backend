from django.urls import path
from .views import RandomCatImageAPI

urlpatterns = [
    path('', RandomCatImageAPI.as_view(), name='random_cat_image_api'),
]
