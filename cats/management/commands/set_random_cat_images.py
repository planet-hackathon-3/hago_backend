from django.core.cache import cache
from django.core.management.base import BaseCommand, CommandError

from cats.models import CatImage


class Command(BaseCommand):
    def handle(self, *args, **options):
        if args:
            raise CommandError("Command doesn't accept any arguments")

        try:
            cat_images = list(CatImage.objects.order_by('?')[:30])
            cache.set('random_cat_image_list', cat_images, 60 * 30)
        except Exception as e:
            self.stderr.write(f"Error occurred: {str(e)}")
        else:
            self.stdout.write(self.style.SUCCESS("Successfully saved random image set"))
