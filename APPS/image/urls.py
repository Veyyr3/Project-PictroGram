# products/urls.py
from django.urls import path

# контроллеры
from image.views import index, add_publication

# имя приложения
app_name = 'image'

urlpatterns = [
    path('', index, name='index'),
    path('add_publication/', add_publication, name='add_publication')
]