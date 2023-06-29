from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from rest_framework.exceptions import ValidationError


class UserAccountManager(BaseUserManager):
    def create(self, email, name, surname=None, password=None, avatar=None):

        email = self.normalize_email(email)
        user = self.model(
            email=email, name=name, surname=surname, avatar=avatar
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, name, surname=None, password=None):
        email = self.normalize_email(email)
        user = self.model(
            email=email, name=name, surname=surname
        )
        user.set_password(password)
        user.save()

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    person_created = models.DateTimeField("Дата создания аккаунта", auto_now=True)
    sex = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to='images/avatars/', blank=True)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"
