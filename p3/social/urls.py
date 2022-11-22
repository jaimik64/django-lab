from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.CreateUser.as_view(), name="CreateUser"),
    path('list/', views.ListUser.as_view(), name='ListUsers'),
    path("user/<int:pk>", views.UserDetail.as_view(), name="UserDetail"),
    path('update/<int:pk>', views.UpdateUser.as_view(), name='UpdateUser'),
    path('delete/<int:pk>', views.RemoveUser.as_view(), name='RemoveUser')
]