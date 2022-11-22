from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from .models import Posts
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import CreatePostForm

# Create your views here.

class ListPosts(ListView):
    model = Posts
    query_resuls = Posts.objects.all()
    template_name = "ListPosts.html"

class CreatePost(CreateView):
    # model = Posts
    # fields = '__all__'
    form_class = CreatePostForm
    template_name = 'CreatePost.html'
    success_url = reverse_lazy('ListPosts')

class UpdatePost(UpdateView):
    model = Posts
    # fields = '__all__'
    form_class = CreatePostForm
    template_name = 'UpdatePost.html'
    success_url = reverse_lazy('ListPosts')

class RemovePost(DeleteView):
    model= Posts
    form_class = CreatePostForm
    template_name = 'RemovePost.html'
    success_url = reverse_lazy('ListPosts')
