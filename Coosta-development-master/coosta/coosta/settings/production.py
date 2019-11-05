from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'coosta_db',
        'USER': 'coosta_db_user',
        'PASSWORD': 'coosta_db_pwd',
        'HOST': 'coosta-mysql',  # Set to empty string for localhost.
        'PORT': '3306',  # Set to empty string for default.
        'CONN_MAX_AGE': 600,  # number of seconds database connections should persist for
    }
}

AWS_STORAGE_BUCKET_NAME = 'coostamedialive'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = "http://%s/" % AWS_S3_CUSTOM_DOMAIN
