from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="home-page"),
    path("all-posts", views.PostsView.as_view(), name="all-posts"),
    path("post/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page"),
]
