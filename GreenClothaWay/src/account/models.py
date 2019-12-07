from datetime import timezone

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class AccountManager(BaseUserManager):

    def create_user(self, email, username, password, title, first_name, last_name, street, housenumber, plz, city,
                    country):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        if not password:
            raise ValueError("Users must have a password")
        if not title:
            raise ValueError("Users must have an title")
        if not first_name:
            raise ValueError("Users must have an first name")
        if not last_name:
            raise ValueError("Users must have an last name")
        if not street:
            raise ValueError("Users must have a street")
        if not housenumber:
            raise ValueError("Users must have a house number")
        if not plz:
            raise ValueError("Users must have a zipcode")
        if not city:
            raise ValueError("Users must have a city")
        if not country:
            raise ValueError("Users must have a country")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            title=title,
            first_name=first_name,
            last_name=last_name,
            street=street,
            housenumber=housenumber,
            plz=plz,
            city=city,
            country=country,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, title, first_name, last_name, street, housenumber, plz, city, country):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            title=title,
            first_name=first_name,
            last_name=last_name,
            street=street,
            housenumber=housenumber,
            plz=plz,
            city=city,
            country=country,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)

    MALE_OR_FEMALE = (
        ('MA', 'Male'),
        ('FE', 'Female'),
    )

    username = models.CharField(max_length=35, unique=True)
    email = models.EmailField(verbose_name="email", max_length=254, unique=True)
    password1 = models.CharField(max_length=50, blank=False)
    password2 = models.CharField(max_length=50, blank=False)
    mail_confirmed = models.BooleanField(default=False)

    title = models.CharField(max_length=20, choices=MALE_OR_FEMALE)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    street = models.CharField(max_length=20)
    plz = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    housenumber = models.CharField(max_length=3)

    rating = models.CharField(max_length=10)
    sells = models.CharField(max_length=10)
    inserations = models.CharField(max_length=10)
    co2 = models.CharField(max_length=10)

    objects = AccountManager()
    USERNAME_FIELD = 'email'
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
