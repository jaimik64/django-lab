from django.urls import path
from . import views

urlpatterns = [
    path('displayPost',views.displayPost,name="displayPost"),
    path('updatePost/<int:pk>',views.updatePost,name="updatePost"),
    path('createPost',views.createPost,name="createPost"),
    path('delete/<int:pk>',views.deletePost,name="deletePost"),
    path('myPost',views.myPost,name="myPost"),
]