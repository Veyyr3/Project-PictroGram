# main urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

# импорт контроллеров

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('image.urls', namespace='image')),
    path('users/', include('users.urls', namespace='users'))
]

# если в режиме разработки
if settings.DEBUG:
    # добавить место хранения фотографий записей из БД
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 