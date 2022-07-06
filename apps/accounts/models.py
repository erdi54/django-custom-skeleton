from django.db import models
from django.contrib.auth.models import \
    BaseUserManager, \
    AbstractBaseUser, \
    PermissionsMixin
from django.utils.translation import gettext_lazy as _

from ..core.models import TimeTrackedModel


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, is_active=False):
        if not email:
            raise ValueError("Her Kullanıcı bir email adresine sahip olmalı.")
        if not username:
            raise ValueError("Kullanıcı bir kullanıcı adı olmalı.")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            is_active=is_active,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )

        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin, TimeTrackedModel):
    last_login = models.DateTimeField(verbose_name=_("Last Login"), auto_now_add=True)
    is_active = models.BooleanField(default=False, verbose_name=_("Is Active?"), blank=True)
    is_admin = models.BooleanField(default=False, verbose_name=_("Admin?"), blank=True)
    verification_token = models.CharField(max_length=255, blank=True, verbose_name=_("Verification Code"))
    password_reset_token = models.CharField(max_length=255, blank=True, verbose_name=_("Password Reset Token"))
    first_name = models.CharField(max_length=255, verbose_name=_("Name"), blank=False, default="")
    last_name = models.CharField(max_length=255, verbose_name=_("Surname"), blank=False, default="")
    email = models.EmailField(verbose_name=_("E-mail"), blank=True, null=True, unique=True, default=None)
    username = models.SlugField(verbose_name="Username", unique=True, blank=True, null=True)
    deleted = models.BooleanField(verbose_name=_("User Deletion Request"), default=False, blank=True)
    api_permissions = models.BooleanField(verbose_name=_("API Permission"), default=False, blank=True)
    is_staff = models.BooleanField(default=False, verbose_name=_("Is Staff?"), blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return f"{self.id} - {self.get_anon_name}"

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    @property
    def get_first_letters(self):
        return f"{self.first_name[0]} {self.last_name[0]}"

    @property
    def get_anon_name(self):
        return f"{self.first_name} {self.last_name[0] if len(self.last_name) else ''}."

    @property
    def is_superuser(self):
        return self.is_admin


class BlackList(TimeTrackedModel):
    ip_address = models.GenericIPAddressField(_("IP address"))

    def __str__(self):
        return self.ip_address
