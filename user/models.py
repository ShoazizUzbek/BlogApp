from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from user.managers import UserManager


class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(
        max_length=25,
        unique=True,
        verbose_name='Username'
    )
    phone = models.CharField(
        max_length=15,
        verbose_name='Phone number'
    )

    fullname = models.CharField(
        max_length=60,
        verbose_name='Full name of User',
        null=True,blank=True
    )
    added_at = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone']

    @property
    def is_staff(self):
        return self.is_superuser

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user'
# Create your models here.
