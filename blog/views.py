from django.shortcuts import render, get_object_or_404,redirect
from .models import Post, Category, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CommentForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def home(request):
    posts_list = Post.objects.all().order_by('-id')
    paginator = Paginator(posts_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'posts/home.html', {'posts': posts})

def category_posts(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    posts_list = Post.objects.filter(category=category).order_by('-id')
    paginator = Paginator(posts_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'posts/category_posts.html', {'posts': posts, 'category': category})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.user = request.user
                comment.save()
                return redirect('post_detail', post_id=post.id)
        else:
            form = CommentForm()

        return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments, 'form': form})
    else:
        return render(request, 'posts/login_required.html', {'post': post})


def register(request):
    status=request.user.is_authenticated
    if not status:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserCreationForm()
        return render(request, 'posts/register.html', {'form': form})
    else:
        return redirect('home')

@login_required
def profile_view(request):
    return render(request, 'posts/profile.html', {'user': request.user})

def search(request):
    query = request.GET.get('q')
    posts_list = Post.objects.filter(title__icontains=query).order_by('-id')
    paginator = Paginator(posts_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'posts/search.html', {'posts': posts})