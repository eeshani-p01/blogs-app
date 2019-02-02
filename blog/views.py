from django.shortcuts import render     # render html templates
from django.http import HttpResponse    # handle request of user

# Create your views here.
def home(request):
    #will return an http response
    return render(request, 'blog/home.html')        # args pass request, template name and data(context)

def about(request):
    #will return an http response
    #return HttpResponse('<h1>About View</h1>')
    return render(request, 'blog/about.html')
