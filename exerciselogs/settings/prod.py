""" DEV specific settings file. """
import os
import django_heroku
import dj_database_url
from .base import *  # noqa: F403

print("--- Loading Production Environment ---")

DEBUG = False

SECRET_KEY = 'xi=!1#dvxj6isfk4l!fx%%%zydmq**577qgsh^5wp8y7cgd!&s'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}
