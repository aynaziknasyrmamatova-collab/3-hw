from core.settings.base import *
import os

DEBUG = True

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "django-insecure-local-development-only-key",
)

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
