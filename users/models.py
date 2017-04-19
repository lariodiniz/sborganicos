# coding=utf-8

import re

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        _('Nickname / User'), max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                _('Enter a valid username. This value should contain only letters, numbers, and characters: @/ ./+/_ .'), _('invalid')
            )
        ], help_text=_('A short name that will be used to uniquely identify it on the platform')
    )

    name = models.CharField(_('name'), max_length=100, blank=True)
    email = models.EmailField(_('E-mail'), unique=True)
    is_staff = models.BooleanField(_('Staff'), default=False)
    is_active = models.BooleanField(_('Active'), default=True)
    date_joined = models.DateTimeField(_('Entry date'), auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]
