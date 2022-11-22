from curses.ascii import HT
from datetime import datetime
from django.shortcuts import render
from datetime import datetime

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')


def demo(request):
    t = datetime.now()
    return HttpResponse(t)