from django.shortcuts import render
from datetime import date
from .models import Post

# just added for now. Later these will be pulled from a database
all_posts = []


def get_date_from_posts(post):
    return post['date']


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, 'blogapp/index.html', {
        "posts": latest_posts
    })


def posts(request):
    all_posts = Post.objects.all()
    return render(request, 'blogapp/all-posts.html', {
        'all_posts': all_posts
    })


def post_detail(request, slug):
    # best practice in python. Basically will give what we want. search and explore about this in google!
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blogapp/post-detail.html', {
        'post': identified_post
    })
