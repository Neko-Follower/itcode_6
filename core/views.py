from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def hello(request):
    return HttpResponse(content='hello world')

def index(request):
    return render(request, 'index.html')

def workers(request):
    return render(request, 'workers.html')

def best_worker(request):
    return render(request, 'best_worker.html')
