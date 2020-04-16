from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _ # for verbose_name
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(_('Email '), unique=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=100, null=True, blank=True)


    USERNAME_FIELD = "username"
    # REQUIRED_FIELDS = ["email",]

