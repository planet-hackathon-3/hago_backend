import requests

from django.core.management.base import BaseCommand, CommandError

from cats.models import CatImage


class Command(BaseCommand):
    def handle(self, *args, **options):
        if args:
            raise CommandError("Command doesn't accept any arguments")

        paylaod = {
            'limit': 30,
        }

        response = requests.get('https://api.thecatapi.com/v1/images/search', params=paylaod).json()
        cat_image_list = []
        for image_json in response:
            cat_image_list.append(
                CatImage(
                    url=image_json['url'],
                    id_for_api=image_json['id'],
                )
            )

        CatImage.objects.bulk_create(cat_image_list)
        self.stdout.write(self.style.SUCCESS(f"Successfully created CatImage objects ({len(cat_image_list)})"))
