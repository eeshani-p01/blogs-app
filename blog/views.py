from django.shortcuts import render
from django.http import HttpResponse    # handle request of user

# Create your views here.
def home(request):
    #will return an http response
    return HttpResponse('<h1>Hello World</h1>')

