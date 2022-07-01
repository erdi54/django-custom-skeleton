from django.apps import AppConfig


class DbLoggerAppConfig(AppConfig):
    name = 'monitoring'
    verbose_name = 'Db Logging'
    # Explicitly set default auto field type to avoid migrations in Django 3.2+
    default_auto_field = 'django.db.models.AutoField'
