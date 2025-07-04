# products/urls.py
from django.urls import path

# контроллеры
from users.views import profile, profile_other, subscriptions, login

# имя приложения
app_name = 'users'

urlpatterns = [
    path('', profile, name='profile'),
    path('profile_other/', profile_other, name='profile_other'),
    path('subscriptions/', subscriptions, name='subscriptions'),

    # авторизация, регистрация
    # path('subscriptions/', subscriptions, name='subscriptions'),
    path('login/', login, name='login'),
]