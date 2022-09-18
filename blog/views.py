from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post, category
# Create your views here.
def home(request):
    # load all the post from db(10)
    posts = Post.objects.all()[:11]
    # print(posts)

    cats = category.objects.all()

    data = {
        'posts': posts,
        'cats': cats
    }
    return render(request, 'home.html', data)


def post(request, url):
    post = Post.objects.get(url=url)
    cats = category.objects.all()

    # print(post)
    return render(request, 'posts.html', {'post': post, 'cats': cats})

def Category(request, url):
    cat = category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html", {'cat': cat, 'posts': posts})
