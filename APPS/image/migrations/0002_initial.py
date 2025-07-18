# Generated by Django 5.2.3 on 2025-07-04 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to='users.user', verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='images',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_images', to='users.user', verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='comments',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_comments', to='image.images', verbose_name='Фото'),
        ),
        migrations.AddField(
            model_name='likes',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_likes', to='image.images', verbose_name='Фото с лайками'),
        ),
        migrations.AddField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_likes', to='users.user', verbose_name='Лайкнувший пользователь'),
        ),
        migrations.AlterUniqueTogether(
            name='likes',
            unique_together={('user', 'image')},
        ),
    ]
