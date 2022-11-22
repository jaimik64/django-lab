from django.urls import path
from . import views

urlpatterns = [
    path('',views.mainPage,name="mainPage"),
    path('extraData',views.extraData,name="extraData"),
]