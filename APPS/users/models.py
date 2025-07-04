# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser # импортировать модель пользователей

# Наследуется от AbstractUser
class User(AbstractUser):
    # описание
    bio = models.TextField(blank=True, null=True)
    # аватар
    avatar = models.ImageField(upload_to='users_avatars', null=True, blank=True)

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