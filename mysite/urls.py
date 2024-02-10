"""
URL configuration for mysite project.

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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import BlogSitemap
from website import views
from website.sitemaps import WebsiteStaticViewSitemap

sitemaps = {
    'websitestatic': WebsiteStaticViewSitemap,
    'blog': BlogSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("http-test/", views.http_test, name="http-test"),
    # path("json-test/", views.json_test, name="json-test"),
    path("", include("website.urls"), name="website"),
    # path("website/", include("website.urls"), name="website"),
    path("blog/", include("blog.urls"), name="blog"),
    path('summernote/', include('django_summernote.urls')),
    path("sitemap.xml", sitemap, {'sitemaps': sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("robots.txt", include("robots.urls"), name="robots"),
    path("__debug__/", include("debug_toolbar.urls")),
]

# static ('static, 'base / static')
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)