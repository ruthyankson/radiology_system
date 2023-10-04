from .common import *

import os

from dotenv import load_dotenv

load_dotenv()

# DEBUG = False
# PRODUCTION = False
DEBUG = os.environ.get("DEBUG")
PRODUCTION = os.environ.get("PRODUCTION")
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'radiology_system_db',
        'USER': 'postgres',
        'PASSWORD': '5Allofme#8',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'media'),
]

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')