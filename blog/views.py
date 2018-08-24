from .models import Post
from django.utils import timezone
from django.views import View
from django.shortcuts import render, get_object_or_404


def post_list(request):
    postsOfUser = Post.objects.all()
    user = request.user
    if request.user.is_authenticated:
      postsOfUser = user.post_set.all()
    else:
      postsOfUser = None
    return render(request, 'blog/post_list.html', {'posts': postsOfUser})

def display_date(request):
    posts = Post.objects.all()
    dates = [posts.first().published_date]
    dates.pop(0)

    for post in posts:
       dates.append(post.published_date)
    return render(request, 'blog/display_dates.html', {'dates': dates})


def displayInd(request, i):
    post = get_object_or_404(Post, pk=i)
    return render(request, 'blog/display.html', {'post': post})


from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def login(request):
    return render(request, 'blog/login.html', {})