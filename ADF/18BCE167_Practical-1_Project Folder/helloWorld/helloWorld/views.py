from django.http.response import HttpResponse
from django.shortcuts import render
# Create your views here.
def helloWorld(request):
    return HttpResponse("<div> <br> <b> <center> <h1> Hello World </h1></center> <b> </div>")
