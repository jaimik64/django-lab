from django.contrib import admin

# Register your models here.
from .models import Posts

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'description','like', 'dislike', 'image')

admin.site.register(Posts, PostAdmin)