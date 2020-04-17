from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse
from django.utils.text import slugify


class User(AbstractUser):
    phone_number = models.CharField(max_length=12, null=True, blank=True, unique=True)
    address = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        data = f"hello {self.username}"
        slug = slugify(data)
        return reverse("user_detail", kwargs={"id": self.id,"slug":slug})
