from django.contrib import messages
from django.contrib import admin

# jaimik : Admin@123
# Register your models here.
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'birthdate', 'gender', 'is_active')

    ordering = ['name', 'birthdate']

    def active(self, obj):
        return obj.is_active == 1
    active.boolean = True

    def make_active(modeladmin, request, queryset):
        queryset.update(is_active=1)
        messages.success(request, "Selected Record(s) Marked is Active Succesfully!!!")

    def make_inactive(modeladmin, request, queryset):
        queryset.update(is_active=0)
        messages.success(request, "Selected Record(s) Marked is Inactive Succesfully!!!")
    
    admin.site.add_action(make_active,"Make Active")
    admin.site.add_action(make_inactive,"Make Inactive")
    db_table = "New Users"

admin.site.register(User, UserAdmin)