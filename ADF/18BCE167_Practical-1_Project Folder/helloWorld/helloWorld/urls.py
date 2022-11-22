from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.helloWorld, name='helloWorld'),
    path('admin/', admin.site.urls),
]
