from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import CommentForm
from .models import Post, Tag, Category, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

# def blog_view(request, category_name=None, tag_name=None, author_name=None):


def blog_view(request, **kwargs):
    # posts = get_list_or_404(Post, status=True)
    posts = Post.objects.filter(status=True)
    if kwargs.get('category_name'):
        posts = posts.filter(category__name=kwargs['category_name'])
    if kwargs.get('tag_name'):
        posts = posts.filter(tags__name=kwargs['tag_name'])
        print(posts.count())
        # my_posts = posts.filter(tags__name=kwargs['tag_name'])
        # posts = posts.filter(tags__name__in=kwargs['tag_name'])
        # print(kwargs['tag_name'])
        # print(posts.count())
        # print(my_posts.count())
    if kwargs.get('author_name'):
        posts = posts.filter(author__username=kwargs['author_name'])
    paginator = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = paginator.get_page(page_number)
    except PageNotAnInteger:
        posts = paginator.get_page(1)
    except EmptyPage:
        posts = paginator.get_page(paginator.num_pages)
    categories = Category.objects.all()
    # tags = Tags.objects.all()
    context = {
        # 'tags': tags,
        'categories': categories,
        'posts': posts,
    }
    if request.user.is_authenticated:
        # context += {
        #     'user': request.user
        # }
        context['user'] = request.user
    return render(request, 'blog/blog-home.html', context)

# def category_blog_view(request, category_name):
#     # posts = get_list_or_404(Post, category=category_name, status=True)
#     posts = Post.objects.filter(status=True)
#     posts = posts.filter(category__name=category_name)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
#     context = {
#         'posts': posts,
#         'tags': tags,
#         'categories': categories,
#     }
#     return render(request, 'blog/blog-home.html', context)

# def tag_blog_view(request, tag_name):
#     # posts = get_list_or_404(Post, category=category_name, status=True)
#     posts = Post.objects.filter(status=True)
#     posts = posts.filter(tag__name=tag_name)
#     categories = Category.objects.all()
#     tags = Tag.objects.all()
#     context = {
#         'posts': posts,
#         'tags': tags,
#         'categories': categories,
#     }
#     return render(request, 'blog/blog-home.html', context)


def blog_single(request):
    # post = Post.objects.get(id=3)
    post = get_object_or_404(Post, pk=3, status=True)
    comments = Comment.objects.filter(
        post=post.id, approved=True).order_by('-created_at')
    context = {
        'title': 'Gamba',
        'content': 'lorem ipsum dolor sit amet, consectetur adip, lorem ipsum dolor, lorem ipsum dolor',
        'author': 'Asghar Farhadi',
        'post': post,
        'comments': comments,
    }
    if request.user.is_authenticated:
        # context += {
        #     'user': request.user
        # }
        context['user'] = request.user
    return render(request, 'blog/blog-single.html', context)


def test_view(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(status=1)
    context = {
        'title': 'Gamba',
        'subtitle': 'Ozaka',
        'content': 'lorem ipsum dolor sit amet, consectetur adip, lorem ipsum dolor, lorem ipsum dolor', 'author': 'ASghar Farhadi',
        'posts': posts
    }
    return render(request, 'test_view.html', context)


def name_tester(request, name):
    # posts = Post.objects.all()
    posts = Post.objects.filter(status=True)
    context = {
        'title': 'Gamba',
        'subtitle': 'Ozaka',
        'content': 'lorem ipsum dolor sit amet, consectetur adip, lorem ipsum dolor, lorem ipsum dolor',
        'author': 'Asghar Farhadi',
        'posts': posts,
        'name': name,
    }
    return render(request, 'test_view.html', context)


def name_family_tester(request, name, family):
    # posts = Post.objects.all()
    posts = Post.objects.filter(status=True)
    context = {
        'title': 'Gamba',
        'subtitle': 'Ozaka',
        'content': 'lorem ipsum dolor sit amet, consectetur adip, lorem ipsum dolor, lorem ipsum dolor',
        'author': 'Asghar Farhadi',
        'posts': posts,
        'name': name,
        'family': family
    }
    return render(request, 'test_view.html', context)


def name_family_age_tester(request, name, family, age):
    # posts = Post.objects.all()
    posts = Post.objects.filter(status=True)
    context = {
        'title': 'Gamba',
        'subtitle': 'Ozaka',
        'content': 'lorem ipsum dolor sit amet, consectetur adip, lorem ipsum dolor, lorem ipsum dolor',
        'author': 'Asghar Farhadi',
        'posts': posts,
        'name': name,
        'family': family,
        'age': age
    }
    return render(request, 'test_view.html', context)


def single_blog(request, pid):
    # posts = Post.objects.all()
    tags = Tag.objects.all()
    if request.method == 'POST':
        nxt = request.Post.get("next", None)
        # post = Post.objects.get(id=pid)
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            print("form.is_valid()")
            messages.success(
                request, 'Your Message has been sent successfully!')
        else:
            print("form.is_not_valid()")
            messages.warning(
                request, 'Your Message has not been sent successfully!')
        # print(f"comments.count() = {comments.count()}")
    else:
        form = CommentForm()
    post = get_object_or_404(Post, pk=pid, status=True)
    if post.login_require:
        return redirect("accounts:login_view")
    categories = Category.objects.all()
    comments = Comment.objects.filter(
        post=post.id, approved=True).order_by('-created_at')
    context = {
        'title': 'Gamba',
        'subtitle': 'Ozaka',
        'content': 'lorem ipsum dolor sit amet, consectetur adip, lorem ipsum dolor, lorem ipsum dolor',
        'author': 'Asghar Farhadi',
        # 'pid': pid,
        'post': post,
        # 'tags': tags,
        'categories': categories,
        'comments': comments,
        'form': form,
    }
    if request.user.is_authenticated:
        # context += {
        #     'user': request.user
        # }
        # print("request.user.username", request.user.username)
        context['user'] = request.user
    else:
        context['user'] = None
    return render(request, 'blog/blog-single.html', context)


def test_simple(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(status=1)
    context = {'title': 'Gamba',
               'subtitle': 'Ozaka',
               'content': 'lorem ipsum dolor sit amet, consectetur adip, lorem ipsum dolor, lorem ipsum dolor', 'author': 'ASghar Farhadi',
               'posts': posts}
    return render(request, 'test_simple.html', context)


def blog_search(request):
    # posts = get_list_or_404(Post, status=True)
    # pprint.pprint(request.__dict__)
    posts = Post.objects.filter(status=True)
    if request.method == 'GET':
        if s := request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = {
        'posts': posts,
        'tags': tags,
        'categories': categories,
    }
    return render(request, 'blog/blog-home.html', context)


def post_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your Message has been sent successfully!')
        else:
            messages.warning(
                request, 'Your Message has not been sent successfully!')
    else:
        form = CommentForm()
    context = {
        'form': form
    }
    return render(request, 'widgets/comment-post-widget.html', context)
