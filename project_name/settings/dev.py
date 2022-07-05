# Python imports
from os.path import join

# project imports

try:
    from .base import *
except ImportError:
    pass

try:
    from .logging import *
except ImportError:
    pass

try:
    from .i18n import *
except ImportError:
    pass

# uncomment the following line to include i18n


# ##### DEBUG CONFIGURATION ###############################
DEBUG = True

# allow all hosts during development
ALLOWED_HOSTS = ['*']

# adjust the minimal login
LOGIN_URL = 'core_login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'core_login'

# ##### DATABASE CONFIGURATION ############################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}',
        'PASSWORD': '123456',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

# ##### APPLICATION CONFIGURATION #########################
INSTALLED_APPS = DEFAULT_APPS
