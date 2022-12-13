from django.shortcuts import render, get_object_or_404
from .models import Post


def starting_page(request):
    latest_posts = Post.objects.all().order_by(
        "-date")[:3]     # -date means descending order
    return render(request, 'blogapp/index.html', {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, 'blogapp/all-posts.html', {
        'all_posts': all_posts
    })


def post_detail(request, slug):
    try:
        identified_post = get_object_or_404(Post, slug=slug)
        return render(request, 'blogapp/post-detail.html', {
            'post': identified_post
        })
    except:
        return render(request, '404.html')
