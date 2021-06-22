from django.contrib.auth.models import AbstractUser
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from home.models import Category, Post
from home.forms import AddPostForm

# Create your views here.



def home(request, category_id=None, page=1):
    context = {
        'title': "Welcome to Blog Home!",
        'categories': Category.objects.all(),
        'posts': Post.objects.all(),
        'category_selected': 0,
    }
    # posts = Post.objects.all()
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


def category_filter(request, page=None, category_id=None):
    context = {
        'title': "Welcome to Blog Home!",
        'categories': Category.objects.all(),
        'posts': Post.objects.all(),
        'category_selected': 0,
    }

    if category_id:
        # posts = Post.objects.filter(category_id=category_id)
        posts = Category.objects.filter(category_id=category_id).post_set.all()
    # else:
    #     posts = Post.objects.all()

    paginator = Paginator(posts, 3)
    post_paginator = paginator.page(page)
    context.update({'posts': post_paginator})
    return render(request, 'home/home.html', context)


def addpost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                # Post.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                print(form)
                form.add_error(None, 'Ошибка добавления поста')
    else:
        form = AddPostForm()
    return render(request, 'home/addpost.html', {'title': "Добавление поста", 'form': form})




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


