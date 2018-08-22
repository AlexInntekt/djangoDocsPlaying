from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})

def display(request):
    posts = Post.objects.all()
    dates = [posts.first().published_date]
    dates.pop(0)

    for post in posts:
       dates.append(post.published_date)
    return render(request, 'blog/display.html', {'dates': dates})