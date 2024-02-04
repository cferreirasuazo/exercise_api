""" DEV specific settings file. """
import os
import django_heroku
import dj_database_url
from .base import *  # noqa: F403

print("--- Loading Production Environment ---")

DEBUG = False

SECRET_KEY = 'xi=!1#dvxj6isfk4l!fx%%%zydmq**577qgsh^5wp8y7cgd!&s'

DATABASE_URL = os.getenv("DATABASE_URL")

DATABASES = {
    "default": dj_database_url.config(default=DATABASE_URL),
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FOWARDED_PROTO', 'https')

django_heroku.settings(locals())