from .base import *
from decouple import config

DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0', ]

DATABASES = {
    "default": {
        "ENGINE": config("SQL_ENGINE"),
        "NAME": config("SQL_DATABASE"),
        "USER": config("SQL_USER"),
        "PASSWORD": config("SQL_PASSWORD"),
        "HOST": config("SQL_HOST"),
        "PORT": config("SQL_PORT")
    }
}

STATIC_ROOT = '/static/'
