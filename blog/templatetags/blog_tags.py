import datetime
from django import template

from blog.models import Post


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
