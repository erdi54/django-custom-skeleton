# Python imports
from os.path import join

# project imports
from .base import PROJECT_ROOT, DEFAULT_APPS

# uncomment the following line to include i18n
# from .i18n import *


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
        'NAME': PROJECT_ROOT,
        'USER': 'streamtotext',
        'PASSWORD': '123456',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}

# ##### APPLICATION CONFIGURATION #########################
INSTALLED_APPS = DEFAULT_APPS
