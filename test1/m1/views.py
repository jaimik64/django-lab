# import datetime
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    t = datetime.now()
    return HttpResponse(t)