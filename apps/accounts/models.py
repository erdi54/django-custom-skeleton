from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        BaseUserManager)
from rest_framework.authtoken.models import Token
from apps.core.models import TimeTrackedModel
from apps.utils.fields import ShortUUIDField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=UserManager.normalize_email(email),
            is_staff=False, is_active=True, is_superuser=False,
            last_login=now, date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        u = self.create_user(email, password, **extra_fields)
        u.is_staff = True
        u.is_active = True
        u.is_superuser = True
        u.save(using=self._db)
        return u


class User(AbstractBaseUser, PermissionsMixin, TimeTrackedModel):
    """
    Users within the Django authentication system are represented by this
    model.
    Email and password are required. Other fields are optional.
    """
    uid = ShortUUIDField(help_text=_("The unique ID under which the"
                                     " accounts is to be accessed."))
    email = models.EmailField(_('email address'), unique=True, max_length=254)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the accounts can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this accounts should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    api_permissions = models.BooleanField(verbose_name=_("API Permission"), default=False, blank=True)
    phone = models.CharField(max_length=50, unique=True, verbose_name=_("Phone"), null=True, blank=True)
    email_notification = models.BooleanField(verbose_name=_("E-mail Notification"), default=True, blank=True)
    mobile_notification = models.BooleanField(verbose_name=_("Mobile Notification"), default=True, blank=True)
    sms_notification = models.BooleanField(verbose_name=_("SMS Notification"), default=True, blank=True)
    cookie_permissions = models.BooleanField(verbose_name=_("Cookie Permission"), default=False, blank=True)
    deleted = models.BooleanField(verbose_name=_("User Deletion Request"), default=False, blank=True)
    api_permissions = models.BooleanField(verbose_name=_("API Permission"), default=False, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = _('accounts')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the accounts."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def __unicode__(self):
        return self.email


# every accounts to have an automatically generated Token
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
