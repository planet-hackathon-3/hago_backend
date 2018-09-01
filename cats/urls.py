from django.urls import path
from .views import RandomCatImageAPI, LikeCatImage, CatImageDetailAPI

urlpatterns = [
    path('', RandomCatImageAPI.as_view(), name='random_cat_image'),
    path('<int:image_id>', CatImageDetailAPI.as_view(), name='cat_image_detail'),
    path('<int:image_id>/like/', LikeCatImage.as_view(), name='like_cat_image'),
]
