from django.shortcuts import get_list_or_404, render, get_object_or_404
from blog.models import Post, Tag, Category

# Create your views here.


def blog_view(request):
    posts = get_list_or_404(Post, status=True)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'posts': posts,
        'tags': tags,
        'categories': categories,
    }
    return render(request, 'blog/blog-home.html', context)


def blog_single(request):
    # post = Post.objects.get(id=3)
    post = get_object_or_404(Post, pk=3, status=True)
    context = {'title': 'Gamba',
               'content': 'lorem ipsum dolor sit amet, consectetur adip, lorem ipsum dolor, lorem ipsum dolor',
               'author': 'Asghar Farhadi',
               'post': post,
               }
    return render(request, 'blog/blog-single.html', context)


def test_view(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(status=1)
    context = {'title': 'Gamba',
               'subtitle': 'Ozaka',
               'content': 'lorem ipsum dolor sit amet, consectetur adip, lorem ipsum dolor, lorem ipsum dolor', 'author': 'ASghar Farhadi',
               'posts': posts}
    return render(request, 'test_view.html', context)


def name_tester(request, name):
    # posts = Post.objects.all()
    posts = Post.objects.filter(status=True)
    context = {'title': 'Gamba',
               'subtitle': 'Ozaka',
               'content': 'lorem ipsum dolor sit amet, consectetur adip, lorem ipsum dolor, lorem ipsum dolor',
               'author': 'Asghar Farhadi',
               'posts': posts,
               'name': name, }
    return render(request, 'test_view.html', context)


def name_family_tester(request, name, family):
    # posts = Post.objects.all()
    posts = Post.objects.filter(status=True)
    context = {'title': 'Gamba',
               'subtitle': 'Ozaka',
               'content': 'lorem ipsum dolor sit amet, consectetur adip, lorem ipsum dolor, lorem ipsum dolor',
               'author': 'Asghar Farhadi',
               'posts': posts,
               'name': name,
               'family': family}
    return render(request, 'test_view.html', context)


def name_family_age_tester(request, name, family, age):
    # posts = Post.objects.all()
    posts = Post.objects.filter(status=True)
    context = {'title': 'Gamba',
               'subtitle': 'Ozaka',
               'content': 'lorem ipsum dolor sit amet, consectetur adip, lorem ipsum dolor, lorem ipsum dolor',
               'author': 'Asghar Farhadi',
               'posts': posts,
               'name': name,
               'family': family,
               'age': age}
    return render(request, 'test_view.html', context)


def single_blog(request, pid):
    # posts = Post.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    posts = Post.objects.filter(status=True)
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk=pid, status=True)
    context = {
        'title': 'Gamba',
        'subtitle': 'Ozaka',
        'content': 'lorem ipsum dolor sit amet, consectetur adip, lorem ipsum dolor, lorem ipsum dolor',
        'author': 'Asghar Farhadi',
        'posts': posts,
        'pid': pid,
        'post': post,
        'tags': tags,
        'categories': categories,
    }
    return render(request, 'blog/blog-single.html', context)
