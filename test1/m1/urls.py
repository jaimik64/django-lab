from importlib.resources import path
from . import views
from django.urls import path

urlpatterns = [
    path('m1',views.index)    
]
