release: python manage.py migrate --noinput
release: python manage.py save_cat_images
release: python manage.py set_random_cat_images
web: gunicorn hago.wsgi --log-file -
