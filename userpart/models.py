from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models
from .img_work import image_resize


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


def user_directory_path(instance, filename):
    # сохраним аватарку юзера в папке с уникальным именем (в идеале по его id)
    # но так как еще не создан объект (пользователь), мы не можем обратится к id, возмем почту до '@'
    return 'user_{0}/{1}'.format(instance.email.partition('@')[0], filename)


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    person_created = models.DateTimeField("Дата создания аккаунта", auto_now=True)
    sex = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.FileField(upload_to=user_directory_path, blank=True, null=True)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"

    # изменим размер картинки, чтобы стандартизировать всех пользователей. Логику будет в файле img_work(image_resize)
    def save(self, commit=True, *args, **kwargs):
        if commit:
            image_resize(self.avatar, 250, 250)
            super().save(*args, **kwargs)

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователи"
        verbose_name_plural = "Пользователи"
