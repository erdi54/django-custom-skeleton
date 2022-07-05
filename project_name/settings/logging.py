LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s %(accounts)s'
        },
        'simple': {
            'format': '%(levelname)s %(asctime)s %(message)s '
        },
    },
    'handlers': {
        'debug_handler': {
            'level': 'DEBUG',
            'class': 'apps.monitoring.db_log_handler.DatabaseLogHandler',
            'formatter': 'simple'
        },

        'error_handler': {
            'level': 'ERROR',
            'class': 'apps.monitoring.db_log_handler.DatabaseLogHandler',
            'formatter': 'simple'
        },
        'fatal_handler': {
            'level': 'FATAL',
            'class': 'apps.monitoring.db_log_handler.DatabaseLogHandler',
            'formatter': 'simple'
        },
        'info_handler': {
            'level': 'INFO',
            'class': 'apps.monitoring.db_log_handler.DatabaseLogHandler',
            'formatter': 'simple'
        }

    },
    'loggers': {
        'general': {
            'handlers': ['debug_handler', 'info_handler', 'fatal_handler', 'error_handler'],
            'level': 1
        },
    },
}

DJANGO_DB_LOGGER_ENABLE_FORMATTER = True
DJANGO_DB_LOGGER_ADMIN_LIST_PER_PAGE = 30
