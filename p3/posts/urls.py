from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ListPosts.as_view(), name="ListPosts"),
    path('create/', views.CreatePost.as_view(), name="CreatePost"),
    path('update/<int:pk>', views.UpdatePost.as_view(), name="UpdatePost"),
    path('delete/<int:pk>', views.RemovePost.as_view(), name="RemovePost")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
