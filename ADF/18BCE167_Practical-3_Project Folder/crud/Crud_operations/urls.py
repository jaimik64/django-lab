from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListCRUD.as_view(),name="CRUD_list"),
    path('Update/<int:pk>',views.UpdateCRUD.as_view(),name="CRUD_update"),
    path('create/',views.CreateCRUD.as_view(),name="CRUD_create"),
    path('Delete/<int:pk>',views.DeleteCRUD.as_view(),name="CRUD_delete"),
    path('Detail/<int:pk>',views.DetailCRUD.as_view(),name="CRUD_detail"),
]