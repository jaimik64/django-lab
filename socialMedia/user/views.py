from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import User

class UserList(ListView):
    model = User

class UserDetail(DetailView):
    model = User

class UserCreate(CreateView):
    model = User

class UserUpdate(UpdateView):
    model = User

class UserDelete(DeleteView):
    model = User