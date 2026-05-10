from .base import *

SECRET_KEY = "django-insecure-(-!$az5r7*1xl%4)$8kar=hmv#d#3&fe)4o2^*@m(%+z5_8ct@"

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("POSTGRES_DB", "game_site"),
        "USER": os.getenv("POSTGRES_USER", "game_site"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", "abc123!"),
        "HOST": os.getenv("POSTGRES_HOST", "localhost"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}