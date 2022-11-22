from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView
from .models import CRUD
from django.urls import reverse_lazy

class CreateCRUD(CreateView):
    model=CRUD
    fields=('First_Name','Middle_Name','Last_Name','Age','Gender','Address','Emai_Id','Mobile_Number','Alternate_Email_Id','Alternate_Mobile_Number','Father_Name','Mother_Name','Institute_Name','Branch_Name')
    template_name="Crud_operations/CRUD_Create.html"
    success_url=reverse_lazy('CRUD_list')
    context_object_name="Crud_operations"

class UpdateCRUD(UpdateView):
    model=CRUD
    fields=('First_Name','Middle_Name','Last_Name','Age','Gender','Address','Emai_Id','Mobile_Number','Alternate_Email_Id','Alternate_Mobile_Number','Father_Name','Mother_Name','Institute_Name','Branch_Name')
    template_name="Crud_operations/CRUD_Update.html"
    success_url=reverse_lazy('CRUD_list')
    context_object_name="Crud_operations"

class DeleteCRUD(DeleteView):
    model=CRUD
    template_name="Crud_operations/CRUD_Confim_Delete.html"
    success_url=reverse_lazy("CRUD_list")
    context_object_name="Crud_operations"

class ListCRUD(ListView):
    model=CRUD
    template_name="Crud_operations/CRUD_List.html"
    context_object_name="Crud_operations"

class DetailCRUD(DetailView):
    model=CRUD
    template_name="Crud_operations/CRUD_Detail.html"
    context_object_name="Crud_operations"