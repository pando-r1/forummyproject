from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.paginator import Paginator
from home.models import Category, Post
# Create your views here.



def home(request, category_id=None, page=1):
    context = {
        'title': "Welcome to Blog Home!",
        'categories': Category.objects.all(),
        'posts': Post.objects.all(),
        'category_selected': 0,
    }

    if category_id:
        posts = Post.objects.filter(category_id=category_id)
    else:
        posts = Post.objects.all()

    paginator = Paginator(posts, 3)
    post_paginator = paginator.page(page)
    context.update({'posts': post_paginator})
    return render(request, 'home/home.html', context)


def show_post(request, post_id=None):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


# def show_category(request, category_id=None):
#     print(Category.objects.all())
#     context = {
#         # 'categories': Post.objects.filter(category_id=category_id),
#     }
#     if category_id:
#         context.update({'posts': Post.objects.filter(category_id=category_id)}) 
#         context.update({'categories': Category.objects.all()}) 
#     else:
#         context.update({'categories': Category.objects.all()})
#     return render(request, 'home/home.html', context)


