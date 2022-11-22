from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.CreateUser, name="CreateUser"),
    path('list/', views.ListUser, name='ListUsers'),
    path("user/<int:pk>", views.UserDetail, name="UserDetail"),
    path('update/<int:pk>', views.UpdateUser, name='UpdateUser'),
    path('delete/<int:pk>', views.RemoveUser, name='RemoveUser')
]