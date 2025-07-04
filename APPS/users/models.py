# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission # импортировать модель пользователей

# Наследуется от AbstractUser
class User(AbstractUser):
    # описание
    bio = models.TextField(blank=True, null=True)
    # аватар
    avatar = models.ImageField(upload_to='users_avatars', null=True, blank=True)

    # ПОЛЯ groups и user_permissions для исправления бага #
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="custom_user_set",
        related_query_name="custom_user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="custom_user_permissions_set",
        related_query_name="custom_user_permission",
    )

class Subscriptions(models.Model):
    # подписчик
    subscriber = models.ForeignKey("User", verbose_name="Подписчик", on_delete=models.CASCADE, related_name='subscriptions_made')
    # на кого подписались
    subscribed_to = models.ForeignKey("User", verbose_name="На кого подписались", on_delete=models.CASCADE, related_name='subscribers')
    # дата подписки
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # чтобы пользователи не могли подписываться друг на друга несколько раз
        unique_together = ('subscriber', 'subscribed_to')