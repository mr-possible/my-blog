from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views import View
from .models import Post, Comment
from .forms import CommentForm 


class StartingPageView(ListView):
    template_name = "blogapp/index.html"
    model = Post
    context_object_name = "posts"
    ordering = "-date"
        
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    
class PostsView(ListView):
    template_name = "blogapp/all-posts.html"
    model = Post
    ordering = "-date"
    context_object_name = "all_posts"

class SinglePostView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post" : post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": Comment.objects.all().order_by("-id")   # descending order of id
        }
        return render(request, "blogapp/post-detail.html", context)
    
    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(
                reverse("post-detail-page", args=[slug])
            )
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": Comment.objects.all().order_by("-id")   # descending order of id
        }
        return render(request, "blogapp/post-detail.html", context)