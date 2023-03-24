from .base import *
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('TULCEA_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# wq: Determine if we are running off django's testing server
DEBUG_WITH_RUNSERVER = False

ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS', 'creatinginterfaces.demo.52north.org')]


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('TULCEA_DB', 'tulceatool'),
        'USER': os.environ.get('TULCEA_DB_USER', 'tulceatool'),
        'PASSWORD': os.environ.get('TULCEA_DB_PW'),
        'HOST': os.environ.get('TULCEA_DB_HOST', 'db-tulcea'),
        'PORT': os.environ.get('TULCEA_DB_PORT', '5432'),
    }
}
