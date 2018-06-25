import datetime
import math

from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db import IntegrityError
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Post, Comment, User, Profile
from .forms import PostCreateForm, CommentCreateForm, RegisterForm, LoginForm, ProfileForm


def index(request):
    post_list = reversed(Post.objects.order_by('create_date')[:10])
    context = {'post_list': post_list}
    return render(request,'blog/index.html',context)

def detail(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404('Post does not exist')
    else:
        comment_list = Comment.objects.filter(post_id=post_id)
        user_list = User.objects.all()
        context = {'post':post,'comment_list':comment_list,'user_list':user_list}
        return render(request,'blog/detail.html',context)

@login_required
def create_post(request):

    if request.method=='POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = request.user.username
            body = form.cleaned_data['content']
            Post.objects.create(title=title,author=author,body=body)
            return HttpResponseRedirect('/blog/')
    else:
        form = PostCreateForm()

    return render(request, 'blog/create_post.html', {'form':form})

@login_required
def create_comment(request, post_id):

    if request.method=='POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            post = Post.objects.get(pk=post_id)
            author = request.user.username
            author_id = request.user.id
            body = form.cleaned_data['content']
            Comment.objects.create(post=post,author=author,body=body,author_id=author_id)
            return HttpResponseRedirect('/blog/'+str(post_id)+'/')
    else:
        form = CommentCreateForm()

    return render(request, 'blog/create_comment.html', {'form': form})

def register(request):

    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                email = form.cleaned_data['email']
                user = User.objects.create_user(username=username, email=email, password=password)
                Profile.objects.create(user=user,sex='U',age=0,introduction='There is no introduction',have_edited=0)
                return HttpResponseRedirect('/blog/')
            except IntegrityError:
                error_message = 'The username/email have been used'
                return render(request, 'blog/register.html', {'form': form,'error_message':error_message})

    else:
        form = RegisterForm()

    return render(request, 'blog/register.html', {'form': form})

def login(request):

    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/blog/')
            else:
                if user is not None:
                    message = 'No such user'
                else:
                    message = 'User is not active'
                return render(request, 'blog/login.html', {'form': form,'message':message})
    else:
        form = LoginForm()

    return render(request, 'blog/login.html', {'form': form})

@login_required
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/blog/')

@login_required
def view_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    try:
        profile = Profile.objects.get(user_id=user.id)
    except ObjectDoesNotExist:
        profile = Profile.objects.create(user=user,sex='U',age=0,introduction='There is no introduction',have_edited=0)
    days_joined = math.floor((timezone.now()- user.date_joined)/datetime.timedelta(days=1))
    context = {'user': user,'days_joined': days_joined,'profile': profile}
    return render(request, 'blog/profile.html', context)

@login_required
def edit_profile(request, user_id):
    user = User.objects.get(pk=user_id)
    profile = Profile.objects.get(user_id=user.id)
    if not request.user.id == user.id:
        message = 'You cannot edit other users\' profile'
        context = {'user': user, 'profile': profile,'message': message}
        return render(request, 'blog/profile.html', context)
    if request.method=='POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile.sex = form.cleaned_data['sex']
            profile.age = form.cleaned_data['age']
            profile.introduction = form.cleaned_data['introduction']
            profile.have_edited = 1
            profile.save()
            return HttpResponseRedirect('/blog/users/'+str(user.id)+'/')
    else:
        form = ProfileForm()
    return render(request, 'blog/edit_profile.html',{'form':form,'user':user})
