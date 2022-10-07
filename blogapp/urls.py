from django.urls import path
from . import views

urlpatterns = [
    path('', views.starting_page, name="home-page"),
    path('all-posts', views.posts, name="all-posts"),
    path('post/<slug:slug>', views.post_detail, name="post-detail-page"),
]
