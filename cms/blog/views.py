from django.shortcuts import render

posts = [
    {
        'author': 'Osep',
        'title': 'Blog Post 1',
        'content': 'First post',
        'date_posted': 'March 23rd, 2020'
    },
    {
        'author': 'Lul',
        'title': 'Blog Post 2',
        'content': 'Second post',
        'date_posted': 'March 24th, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})