import datetime
from django import template
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from requests import request
from blog.forms import CommentForm
from blog.models import Category, Comment, Post, Tag
from django.contrib import messages


register = template.Library()


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.simple_tag
def hello():
    return 'hello world'


@register.simple_tag(name='plustwo')
def func(a=5):
    return a + 2


@register.simple_tag(name='totalposts')
def posts_count():
    posts = Post.objects.filter(status=1).count()
    return posts


@register.simple_tag(name='posts')
def posts_count():
    posts = Post.objects.filter(status=1)
    return posts

@register.simple_tag(name='comments_count')
def comments_count(pid):
    post = Post.objects.filter(pk=pid)
    comments = Comment.objects.filter(post=post.id)
    return comments.count()

@register.filter
def snippet(value):
    return value[:100]


@register.filter
def snippetarg(value, arg=20):
    return value[:arg]+'...'

# @register.inclusion_tag('popular_posts.html')
# def popularposts():
#     posts = Post.objects.filter(status=1).order_by('-published_at')
#     return {'posts': posts}


@register.inclusion_tag('widgets\popular-post-widget.html')
def popularposts(count=3):
    posts = Post.objects.filter(status=True).order_by('-published_at')[:count]
    return {'posts': posts}


@register.inclusion_tag('widgets\post-category-widget.html')
def categories():
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    categories_count = {}
    for category_name in categories:
        # category_count = Post.objects.filter(category=category_name.name).count()
        # categories_count[category_name.name] = category_count
        category_post = posts.filter(category=category_name).count()
        categories_count[category_name.name] = category_post
    return {'categories_count': categories_count}


@register.inclusion_tag('widgets\\tag-cloud-widget.html')
def tags(post=None):
    posts = Post.objects.filter(status=True)
    # tags = Tag.objects.all()
    tags = Post.tags.all()
    tags_count = []
    tags_post = {}
    for tag_name in tags:
        # category_count = Post.objects.filter(category=category_name.name).count()
        # categories_count[category_name.name] = category_count
        tag_count = posts.filter(tags=tag_name).count()
        if_tag = False
        if post:
            if tag_name in post.tags.all():
                print(f"tag_name = {tag_name} and in post.tags.all")
                if_tag = True
            else:
                print(f"tag_name = {tag_name} and is not in post.tags.all")

        # if tag_name in
        # tags_count[tag_name.name] = {tag_name.name, tag_post, this_tag}
        tags_count.append([tag_name.name, tag_count, if_tag])
    return {'tags_count': tags_count}


@register.inclusion_tag('widgets\\author-widget.html')
def activest_author():
    posts = Post.objects.filter(status=True)
    authors = User.objects.all()
    authors_count = {}
    activest_author = get_object_or_404(User, pk=1)
    for author_name in authors:
        # category_count = Post.objects.filter(category=category_name.name).count()
        # categories_count[category_name.name] = category_count
        author_post_count = posts.filter(author=author_name).count()
        if author_post_count > 0:
            authors_count[author_name] = author_post_count
            activest_author = author_name
    return {'author': activest_author}


@register.inclusion_tag('widgets\\author-widget.html')
def author(author_id=1):
    posts = Post.objects.filter(status=True)
    # post = get_object_or_404(Post, pk=3, status=True)
    author = get_object_or_404(User, pk=author_id)
    authors = User.objects.all()
    authors_count = {}
    for author_name in authors:
        # category_count = Post.objects.filter(category=category_name.name).count()
        # categories_count[category_name.name] = category_count
        author_post_count = posts.filter(author=author_name).count()
        if author_post_count > 0:
            authors_count[author_name] = author_post_count
    return {'author': author}

@register.inclusion_tag('widgets\\comment-post-widget.html')
def post_comment():
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
    return context