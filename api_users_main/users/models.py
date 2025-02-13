from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from .managers import CustomUserManager
# import uuid


class CustomUser(AbstractUser):
    username=None
    email = models.EmailField(unique=True)
    objects = CustomUserManager()
    refresh_token = models.UUIDField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    groups = models.ManyToManyField(
            Group,
            verbose_name=('groups'),
            blank=True,
            help_text=(
                'The groups this user belongs to. A user will get all permissions '
                'granted to each of their groups.'
            ),
            related_name="customuser_set",  # Указываем уникальное имя
            related_query_name="user",
        )
    
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name="customuser_set", # Указываем уникальное имя
        related_query_name="user",
    )