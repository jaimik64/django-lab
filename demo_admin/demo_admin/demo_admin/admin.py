from django.contrib import admin

# Register your models here.
from .models import State
from django.contrib import messages
  
#admin.site.register(State)

class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'created_on')
  
    def active(self, obj):
        return obj.is_active == 1
  
    active.boolean = True
  
    def make_active(modeladmin, request, queryset):
        queryset.update(is_active = 1)
        messages.success(request, "Selected Record(s) Marked as Active Successfully !!")
  
    def make_inactive(modeladmin, request, queryset):
        queryset.update(is_active = 0)
        messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!")
  
    admin.site.add_action(make_active, "Make Active")
    admin.site.add_action(make_inactive, "Make Inactive")  
admin.site.register(State, StateAdmin)