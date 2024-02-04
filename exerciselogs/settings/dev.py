from .base import *
from pathlib import Path
print("--- Loading Dev Environment ---")
DEBUG = True

ALLOWED_HOSTS = ["*"]

SECRET_KEY = 'django-insecure-*v(@owu(r-&a)zanod(72y=hqb*99^sme-=w!r=265j#+qkd!l'

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

