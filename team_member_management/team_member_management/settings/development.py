from .base import *
from decouple import config
import os

SECRET_KEY = "adfadfadfiouu23jo234234"

DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'DEBUG',
        },
    },
    'root': {
        'handlers': ['console'],
    }
}

STATIC_ROOT = '/home/vishal/Documents/datawrkz/Interview_tests/platform_engineer_test/team_member_management/static/'

