
from . import views
from django.urls import path

urlpatterns = [
    path('demo_module1', views.index),
    # path("demo", views.demo)
]
