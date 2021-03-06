import logging
from django.db import models
from six import python_2_unicode_compatible
from django.utils.translation import gettext_lazy as _
from apps.core.models import TimeTrackedModel

LOG_LEVELS = (
    (logging.NOTSET, _('NotSet')),
    (logging.INFO, _('Info')),
    (logging.WARNING, _('Warning')),
    (logging.DEBUG, _('Debug')),
    (logging.ERROR, _('Error')),
    (logging.FATAL, _('Fatal')),
)


@python_2_unicode_compatible
class StatusLog(TimeTrackedModel):
    logger_name = models.CharField(max_length=100)
    level = models.PositiveSmallIntegerField(choices=LOG_LEVELS, default=logging.ERROR, db_index=True)
    msg = models.TextField()
    trace = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.msg

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural = verbose_name = 'Logging'
