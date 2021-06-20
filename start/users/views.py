from django import contrib
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm


# Create your views here.
    # context = {
    #     'title': "Welcome to Blog Home!",
    #     'categories': Category.objects.all(),
    #     'posts': Post.objects.all(),
    # }


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
            form=UserLoginForm()
    context = {'form': form}
    return render(request, 'users/signin.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрировались!')
            return HttpResponseRedirect(reverse('login'))
        else:
            print(form.errors)
    form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form': form}
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('home'))
