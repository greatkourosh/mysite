import datetime
from django import template

from blog.models import Category, Post


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
def categories_count():
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    categories_count = {}
    for category_name in categories:
        # category_count = Post.objects.filter(category=category_name.name).count()
        # categories_count[category_name.name] = category_count
        category_post = posts.filter(category=category_name).count()
        categories_count[category_name.name] = category_post
    return {'categories_count': categories_count}
