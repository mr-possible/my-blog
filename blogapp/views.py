from typing import Any, Dict
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post


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

class SinglePostView(DetailView):
    template_name = "blogapp/post-detail.html"
    model = Post

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context
