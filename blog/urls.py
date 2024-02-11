"""
URL configuration for website app.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import debug_toolbar
from django.conf import settings
from django.urls import path, include
from blog import views
from .feeds import LatestEntriesFeed

app_name = 'blog'
urlpatterns = [
    path("", views.blog_view, name="index"),
    path("category/<str:category_name>", views.blog_view, name="category_blog_view"),
    path("tag/<str:tag_name>", views.blog_view, name="tag_blog_view"),
    path("rss/feed/", LatestEntriesFeed(), name="LatestEntriesFeed"),
    path("author/<str:author_name>", views.blog_view, name="author_blog_view"),
    path("search/", views.blog_search, name="blog_search"),
    path("<int:pid>", views.single_blog, name="single_blog"),
    path("comment", views.post_comment, name="post_comment"),
    path("single", views.blog_single, name="single"),
    path("test_view", views.test_view, name="test_view"),
    path("test_simple", views.test_simple, name="test_simple"),
    path("<str:name>", views.name_tester, name="name_tester"),
    path("<str:name>/<str:family>", views.name_family_tester, name="name_family_tester"),
    path("<str:name>/<str:family>/<int:age>", views.name_family_age_tester, name="name_family_age_tester"),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns