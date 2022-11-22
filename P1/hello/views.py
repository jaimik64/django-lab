from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h2> Hello World</h2>")