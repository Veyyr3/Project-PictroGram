# products/urls.py
from django.urls import path

# контроллеры
from users.views import profile

# имя приложения
app_name = 'users'

urlpatterns = [
    path('', profile, name='profile'),
    # path('add_publication/', add_publication, name='add_publication')
]