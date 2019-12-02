from datetime import timezone, datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


class InserationManager(models.Manager):

    def create_inseration(self, title, username, description, images, category, size):
        if not title:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        if not images:
            raise ValueError("Users must have a password")
        if not category:
            raise ValueError("Users must have an title")
        if not size:
            raise ValueError("Users must have an first name")

        inseration = self.model(
            username=username,
            title=title,
            description=description,
            images=images,
            category=category,
            size=size,
            inserted_at=datetime.now,
        )

        inseration.save(using=self._db)
        return inseration



class Account(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    images = models.ImageField()
    category = models.CharField()
    size = models.DateTimeField(verbose_name="date joined", auto_now_add=True)

    MALE_OR_FEMALE = (
        ('MA', 'Male'),
        ('FE', 'Female'),
    )

    objects = InserationManager()
    REQUIRED_FIELDS = (
        'username', 'password',
        'title', 'first_name', 'last_name',
        'street', 'plz',
        'city', 'country',
        'housenumber',)

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
