from django.contrib import admin

# модели
from users.models import User, Subscriptions

# Register your models here.
admin.site.register(User)

@admin.register(Subscriptions)
class SubscriptionsAdmin(admin.ModelAdmin):
    list_display = ['subscriber', 'subscribed_to', 'created_at']
