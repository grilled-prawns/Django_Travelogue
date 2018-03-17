from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.http import Http404
from urllib.parse import quote_plus
from django.utils import timezone
from .models import Post
from .forms import PostForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def post_list(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    context = {
        'posts' : posts
    }
    return render(request, 'blog_app/index.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk = pk)
    share_string = quote_plus(post.text)
    context = {
        'post' : post,
        'share_string' : share_string,
    }

    return render(request, 'blog_app/detail.html', context)

def new_post(request):


    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            _post = form.save(commit=False)
            _post.author = request.user
            _post.publish_date = timezone.now()
            _post.save()
            return redirect('post_detail', pk = _post.pk)

    else:
        form = PostForm()

        context = {
            'form': form
        }

        return render(request, 'blog_app/new_post.html', context)


def post_update(request, pk):


    instance = get_object_or_404(Post, pk = pk)


    form = PostForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('post_detail', pk=instance.pk)

    context = {
        'form' : form,
    }

    return render(request, 'blog_app/new_post.html', context)

def post_delete(request, pk):

    instance = get_object_or_404(Post, pk=pk)
    instance.delete()

    return redirect('post_list')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')
    else:
        form = SignUpForm()
    return render(request, 'blog_app/signup.html', {'form': form})

# Create your views here.
