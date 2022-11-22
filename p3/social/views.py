from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import User
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.admin.widgets import AdminDateWidget
from social.forms import CreateUserForm
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django import forms


# Create your views here.

# Base View
def home(request):
    # template_name = 'home.html'
    return render(request, 'templates/home.html')


# List Users View
class ListUser(ListView):
    model = User
    query_results = User.objects.all()
    template_name = 'ListUsers.html'

class UserDetail(DetailView):
    model = User
    template_name = 'UserDetail.html'

# Create User 
class CreateUser(CreateView):
    # model= User
    form_class = CreateUserForm
    # fields = '__all__'
    template_name = 'CreateUser.html'
    success_url = reverse_lazy('ListUsers') 

    # to display date picker widget in form
    def get_form(self, form_class=None):
        form = super(CreateUser, self).get_form(form_class)
        form.fields['birthdate'].widget = AdminDateWidget(attrs={'type': 'date'})
        return form

# Update User View
class UpdateUser(UpdateView):
    model = User
    # fields = '__all__'
    form_class = CreateUserForm
    template_name = 'UpdateUser.html'
    success_url = reverse_lazy('ListUsers')


# Remove User View 
class RemoveUser(DeleteView):
    model = User
    form_class = CreateUserForm
    template_name = 'RemoveUser.html'
    success_url = reverse_lazy('ListUsers')