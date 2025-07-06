# image/model.py
from django.db import models

# модель пользователей
from users.models import User

# фото
class Images(models.Model):
    # фото
    image = models.ImageField(upload_to='users_images')
    # название фото
    image_name = models.CharField(max_length=30)
    # описание фото
    description = models.TextField()
    # дата создания
    created_at = models.DateTimeField(auto_now_add=True)
    # пользователь, который сделал фото
    user = models.ForeignKey(to=User, verbose_name="Пользователь", on_delete=models.CASCADE, related_name='user_images')

class Comments(models.Model):
    # содержимое комментария
    body_text = models.TextField()
    # дата создания
    created_at = models.DateTimeField(auto_now_add=True)
    # пользователь, кто сделал комментарий
    user = models.ForeignKey(to=User, verbose_name="Пользователь", on_delete=models.CASCADE, related_name='user_comments')
    # фото на которое был сделан комментарий
    image = models.ForeignKey("Images", verbose_name="Фото", on_delete=models.CASCADE, related_name='image_comments')

class Likes(models.Model):
    user = models.ForeignKey(User, verbose_name='Лайкнувший пользователь', on_delete=models.CASCADE, related_name='user_likes')
    image = models.ForeignKey("Images", verbose_name='Фото с лайками', on_delete=models.CASCADE, related_name='image_likes')

    class Meta:
        # запретить пользователям лайкать дважды
        unique_together = ('user', 'image')
