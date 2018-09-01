from django.db import models
from common.models import TimeStampedModel


class CatImage(TimeStampedModel):
    url = models.URLField('이미지 URL')
    id_for_api = models.CharField('API용 ID', max_length=16, unique=True, db_index=True)
    like_count = models.PositiveIntegerField('좋아요 수', default=0)

    def __str__(self):
        return self.id_for_api


class Tip(TimeStampedModel):
    content = models.TextField('내용')

    def __str__(self):
        return self.id
