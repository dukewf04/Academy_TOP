from django.shortcuts import render
from .models import Posts



def home(request):
    posts = Posts.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/home.html', context)


def about(request):
    return render(request, 'posts/about.html')
