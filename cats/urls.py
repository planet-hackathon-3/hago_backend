from django.urls import path
from .views import (
    RandomCatImageList, LikeCatImage, CatImageDetail, RandomTip,
)

urlpatterns = [
    path('', RandomCatImageList.as_view(), name='random_cat_image'),
    path('<int:image_id>', CatImageDetail.as_view(), name='cat_image_detail'),
    path('<int:image_id>/like/', LikeCatImage.as_view(), name='like_cat_image'),
    path('tip/random/', RandomTip.as_view(), name='random_tip'),
]
