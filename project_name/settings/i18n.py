# Python imports
from os.path import join

# Django imports
from django.utils.translation import gettext_lazy as _

# project imports
from .base import PROJECT_ROOT, MIDDLEWARE

# ##### INTERNATIONALIZATION ##############################

LANGUAGE_CODE = 'tr'
TIME_ZONE = 'Europe/Istanbul'

# Internationalization
USE_I18N = True

# Localisation
USE_L10N = True

# enable timezone awareness by default
USE_TZ = True

# This list of languages will be provided
LANGUAGES = (
    ('tr', _('Turkish')),
    ('en', _('English')),

)

# Look for translations in these locations
LOCALE_PATHS = (
    join(PROJECT_ROOT, 'locale'),
)

# Inject the localization middleware into the right position
MIDDLEWARE = [y for i, x in enumerate(MIDDLEWARE) for y in (
    ('django.middleware.locale.LocaleMiddleware', x) if MIDDLEWARE[
     i - 1] == 'django.contrib.sessions.middleware.SessionMiddleware' else (
     x,))]
