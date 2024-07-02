from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from . forms import UserRegisterForm, PostForm
from django.contrib.auth import logout

def feed(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'social/feed.html', context)

def profile(request):
    return render(request, 'social/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
    else:
        form = UserRegisterForm()

    context = { 'form': form }
    return render(request, 'social/register.html', context)

def custom_logout_view(request):
    logout(request)
    return redirect('login')

def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'post enviado')
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'social/post.html')


