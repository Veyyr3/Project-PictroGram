# products/urls.py
from django.urls import path

# контроллеры
from users.views import profile, profile_other

# имя приложения
app_name = 'users'

urlpatterns = [
    path('', profile, name='profile'),
    path('profile_other/', profile_other, name='profile_other')
]