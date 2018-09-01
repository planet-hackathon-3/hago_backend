from django.db import models
from common.models import TimeStampedModel


class CatImage(TimeStampedModel):
    url = models.URLField('이미지 URL')

    def __str__(self):
        return self.url


class Tip(TimeStampedModel):
    content = models.TextField('내용')

    def __str__(self):
        return self.id
