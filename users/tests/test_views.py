# coding=utf-8

from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.conf import settings

from model_mommy import mommy

