from django.contrib import sitemaps
from django.urls import reverse

from blog.models import Post


class BlogSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'weekly'
    
    def items(self):
        # return ['blog:index',]
        return Post.objects.filter(status=True)
    
    def lastmod(self, obj):
        # return reverse(obj)
        return obj.published_at
    
    # this(Preferred) or def get_absolute_url(self): in models.py
    def location(self, item):
        return reverse('blog:single_blog', kwargs={'pid':item.id})