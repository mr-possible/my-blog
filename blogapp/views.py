from django.shortcuts import render


def starting_page(request):
    return render(request, 'blogapp/index.html')


def posts(request):
    return render(request, 'blogapp/all-posts.html')


def post_detail(request):
    pass
