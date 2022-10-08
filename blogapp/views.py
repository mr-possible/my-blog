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
        "full_content": """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
            It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        
            It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. 
            The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. 
            Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. 
            Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
        """
    },
    {
        "title": "Dummy Title 02",
        "slug": "dummy-slug-seo-term2",
        "image": "sample.jpg",
        "image_alt": "wrfewf",
        "author": "Sambhav Dave",
        "date": date(2022, 7, 11),
        "preview_text": "Dummy Dummy Dummy",
        "full_content": """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
            It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        
            It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. 
            The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. 
            Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. 
            Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
        """
    },
    {
        "title": "Dummy Title 03",
        "slug": "dummy-slug-seo-term3",
        "image": "sample.jpg",
        "image_alt": "ijijji",
        "author": "Sambhav Dave",
        "date": date(2022, 7, 12),
        "preview_text": "Dummy Dummy Dummy",
        "full_content": """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
            It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        
            It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. 
            The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. 
            Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. 
            Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
        """
    },
    {
        "title": "Dummy Title 04",
        "slug": "dummy-slug-seo-term4",
        "image": "sample.jpg",
        "image_alt": "ijijji",
        "author": "Sambhav Dave",
        "date": date(2022, 7, 13),
        "preview_text": "Dummy Dummy Dummy",
        "full_content": """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
            It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        
            It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. 
            The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. 
            Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. 
            Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
        """
    },
    {
        "title": "Dummy Title 05",
        "slug": "dummy-slug-seo-term5",
        "image": "sample.jpg",
        "image_alt": "ijijji",
        "author": "Sambhav Dave",
        "date": date(2022, 7, 14),
        "preview_text": "Dummy Dummy Dummy",
        "full_content": """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
            It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        
            It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. 
            The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. 
            Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. 
            Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
        """
    },
    {
        "title": "Dummy Title 06",
        "slug": "dummy-slug-seo-term6",
        "image": "sample.jpg",
        "image_alt": "ijijji",
        "author": "Sambhav Dave",
        "date": date(2022, 7, 15),
        "preview_text": "Dummy Dummy Dummy",
        "full_content": """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
            Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.
            It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
            It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        
            It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. 
            The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. 
            Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. 
            Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).
        """
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
    # best practice in python. Basically will give what we want. search and explore about this in google!
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, 'blogapp/post-detail.html', {
        'post': identified_post
    })
