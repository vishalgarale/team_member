from .base import *
from decouple import config
from boto3.session import Session

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

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

boto3_session = Session(aws_access_key_id=config('AWS_ACCESS_KEY_ID'),
                        aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY'),
                        region_name=config('AWS_REGION_NAME'))

LOGGING = {
  'version': 1,
  'handlers': {
      'watchtower':  {
          'level': 'DEBUG',  # Or some more appropriate level
          'class': 'watchtower.CloudWatchLogHandler',
          'boto3_session': boto3_session,
      },
  },
  'loggers': {
      'django': {
          'handlers': ['watchtower'],
          'level': 'DEBUG',  # Or some more appropriate level
          'propagate': True,
      },
  }
}
