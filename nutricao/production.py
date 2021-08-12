from .settings import *

import dj_database_url
import os

DEBUG = os.getenv('DEBUG', False)

ALLOWED_HOSTS = ['*']

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

STATIC_ROOT = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
