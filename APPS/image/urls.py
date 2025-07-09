# image/urls.py
from django.urls import path

# контроллеры
from image.views import index, add_publication, like, add_comment

# имя приложения
app_name = 'image'

urlpatterns = [
    path('', index, name='index'),
    path('page/<int:page_number>/', index, name='index_paginated'), # Для последующих страниц
    
    path('add_publication/', add_publication, name='add_publication'), # добавить публикацию

    path('like/<int:image_id>', like, name='like'), # поставить лайк

    path('<int:image_id>/add_comment/', add_comment, name='add_comment'), # добавить комментарий
]