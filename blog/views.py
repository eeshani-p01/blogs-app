from django.shortcuts import render     # render html templates
from django.http import HttpResponse    # handle request of user
from .models import Post

# Data = we have list of dictionary
posts = [
    {
        'author': 'Eeshani Patel',
        'title':' My first post',
        'content': 'My first post description',
        'date_posted': 'January 19, 2019', 
    },
    {
        'author': 'John Callahan',
        'title':' Hello World',
        'content': 'This is Callahan',
        'date_posted': 'February 1, 2018', 
    },
]

# Create your views here.
def home(request):
    # will create a context,i.e dictionary, to pass the data to home template
    context = {
        'posts': Post.objects.all()
    }
    #will return an http response
    return render(request, 'blog/home.html', context)        # args pass request, template name and data(context)

def about(request):
    #will return an http response
    #return HttpResponse('<h1>About View</h1>')
    return render(request, 'blog/about.html', {'title':'About'})
