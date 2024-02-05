from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(
        max_length=255,
        )
    def __str__(self):
        return self.name
    verbose_name = 'Category'
    verbose_name = 'Categories'
        

class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        )
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(
        max_length=255,
        )
    content = models.TextField()
    # tag
    # category
    counted_view = models.IntegerField(
        default=0,
        )
    status = models.BooleanField(
        default=False,
        )
    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        )
    published_at = models.DateTimeField(
        null=True,
        )
    updated_at = models.DateTimeField(
        auto_now=True,
        )
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag)
    
    class Meta:
        ordering = ['-created_at','status']
        # verbose_name = 'پست'
        # verbose_name_plural = 'پست ها'
    def __str__(self):
        return self.title
    
    def snippets(self):
        return self.content[:100] + '...'

    