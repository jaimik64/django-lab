from django.contrib import admin

# Register your models here.
from .models import State
from django.contrib import messages

#admin.site.register(State)

class StateAdmin(admin.ModelAdmin):
    # ModelAdmin also allows us 
    # to create dynamic fields by declaring methods
    list_display = ('name', 'is_active', 'created_on')
    #list_display = ('name', 'is_active', 'created_on', 'updated_on')
    #ordering = ['name']
    #ordering = ['-created_on']
    ordering = ('created_on', 'is_active','name')
    #customize the display by creating a custom 
    # admin model class and setting the value of 
    # list_display property
  
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