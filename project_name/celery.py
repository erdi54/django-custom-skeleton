from __future__ import absolute_import, unicode_literals
import os
from django.conf import settings
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.prod")

app = Celery('{{ project_name }}')
app.config_from_object(settings, namespace='CELERY')
app.autodiscover_tasks()
