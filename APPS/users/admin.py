from django.contrib import admin

# модели
from users.models import User, Subscriptions

# Register your models here.
admin.site.register(User)
admin.site.register(Subscriptions)
