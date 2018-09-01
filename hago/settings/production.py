from .base import *  # NOQA

DEBUG = False

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://h:p2555d203886181df936adca66d4aa1f5204561e6cd4831200ad8230ef8fdf3aa@"
                    "ec2-18-209-253-27.compute-1.amazonaws.com:63879",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}
