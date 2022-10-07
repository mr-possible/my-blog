from django.shortcuts import render
from datetime import date

# just added for now. Later these will be pulled from a database
all_posts = [
    {
        "title": "Dummy Title 01",
        "slug": "dummy-slug-seo-term1",
        "image": "sample.jpg",
        "image_alt": "wewewe",
        "author": "Sambhav Dave",
        "date": date(2022, 7, 10),
        "preview_text": "Dummy Dummy Dummy",
        "full_content": "Full Dummy Content"
    },
    {
        "title": "Dummy Title 02",
        "slug": "dummy-slug-seo-term2",
        "image": "sample.jpg",
        "image_alt": "wrfewf",
        "author": "Sambhav Dave",
        "date": date(2022, 7, 11),
        "preview_text": "Dummy Dummy Dummy",
        "full_content": "Full Dummy Content"
    },
    {
        "title": "Dummy Title 03",
        "slug": "dummy-slug-seo-term3",
        "image": "sample.jpg",
        "image_alt": "ijijji",
        "author": "Sambhav Dave",
        "date": date(2022, 7, 12),
        "preview_text": "Dummy Dummy Dummy",
        "full_content": "Full Dummy Content"
    },
    {
        "title": "Dummy Title 04",
        "slug": "dummy-slug-seo-term4",
        "image": "sample.jpg",
        "image_alt": "ijijji",
        "author": "Sambhav Dave",
        "date": date(2022, 7, 13),
        "preview_text": "Dummy Dummy Dummy",
        "full_content": "Full Dummy Content"
    },
    {
        "title": "Dummy Title 05",
        "slug": "dummy-slug-seo-term5",
        "image": "sample.jpg",
        "image_alt": "ijijji",
        "author": "Sambhav Dave",
        "date": date(2022, 7, 14),
        "preview_text": "Dummy Dummy Dummy",
        "full_content": "Full Dummy Content"
    },
    {
        "title": "Dummy Title 06",
        "slug": "dummy-slug-seo-term6",
        "image": "sample.jpg",
        "image_alt": "ijijji",
        "author": "Sambhav Dave",
        "date": date(2022, 7, 15),
        "preview_text": "Dummy Dummy Dummy",
        "full_content": "Full Dummy Content"
    }
]


def get_date_from_posts(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date_from_posts, reverse=True)
    latest_posts = sorted_posts[:3]
    return render(request, 'blogapp/index.html', {
        "posts": latest_posts
    })


def posts(request):
    return render(request, 'blogapp/all-posts.html', {
        'all_posts': all_posts
    })


def post_detail(request, slug):
    return render(request, 'blogapp/post-detail.html')
