from .models import Post
from django.utils import timezone
from django.views import View
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'blog/post_list.html', {'posts': posts})

def display_date(request):
    posts = Post.objects.all()
    dates = [posts.first().published_date]
    dates.pop(0)

    for post in posts:
       dates.append(post.published_date)
    return render(request, 'blog/display_dates.html', {'dates': dates})


def displayInd(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/display.html', {'post': post})