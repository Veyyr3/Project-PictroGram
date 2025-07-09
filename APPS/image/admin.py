from django.contrib import admin

from image.models import Images, Likes, Comments

# Register your models here.
admin.site.register(Images)
admin.site.register(Likes)
admin.site.register(Comments)
