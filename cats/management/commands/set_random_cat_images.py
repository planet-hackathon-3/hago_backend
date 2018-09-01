import random

from django.core.cache import cache
from django.core.management.base import BaseCommand, CommandError

from cats.models import CatImage


class Command(BaseCommand):
    def handle(self, *args, **options):
        if args:
            raise CommandError("Command doesn't accept any arguments")

        try:
            cat_image_id_list = list(CatImage.objects.values_list('id', flat=True))
            random_image_id_list = random.sample(cat_image_id_list, 30)
            cat_images = CatImage.objects.filter(id__in=random_image_id_list)
            cache.set('random_cat_image_list', cat_images, 60 * 30)
        except Exception as e:
            self.stderr.write(f"Error occurred: {str(e)}")
        else:
            self.stdout.write(self.style.SUCCESS("Successfully saved random image set"))
