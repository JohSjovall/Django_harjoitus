from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post contet',
        'date_post': 'August 27, 2018',
    },
    {
        'author': 'Jonne',
        'title': 'Blog Post 2',
        'content': 'jotain post contet',
        'date_post': 'August 28, 2018',
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')