import datetime
from django import template
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from blog.models import Category, Post, Tag


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
def tags():
    posts = Post.objects.filter(status=True)
    tags = Tag.objects.all()
    tags_count = {}
    for tag_name in tags:
        # category_count = Post.objects.filter(category=category_name.name).count()
        # categories_count[category_name.name] = category_count
        tag_post = posts.filter(tag=tag_name).count()
        tags_count[tag_name.name] = tag_post
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
