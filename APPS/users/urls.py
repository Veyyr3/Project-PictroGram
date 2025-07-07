# users/urls.py
from django.urls import path

# контроллеры
from users.views import profile, profile_other, subscriptions, login, registration, logout, delete_publication, subscribe, unsubscribe

# имя приложения
app_name = 'users'

urlpatterns = [
    path('', profile, name='profile'),

    # работа с чужими профилями
    path('profile_other/<int:user_id>', profile_other, name='profile_other'), # посмотреть профиль других
    path('subscriptions/', subscriptions, name='subscriptions'), # посмотреть свои подписки
    path('subscribe/<int:user_id>', subscribe, name='subscribe'), # подписаться
    path('unsubscribe/<int:user_id>', unsubscribe, name='unsubscribe'), # отписаться


    # авторизация, регистрация
    path('registration/', registration, name='registration'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    # работа с публикациями
    path('delete_publication/<int:image_id>', delete_publication, name='delete_publication')
]