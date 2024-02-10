from django.contrib import admin
from website.models import Contact
from .models import Post, Tag, Category
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = ')`:'
    list_display = ('title', 'status', 'author', 'counted_view', 'published_at',)
    list_filter = ('status', 'author', 'category',)
    ordering = ['-created_at', 'author',]
    search_fields = ['title', 'content', 'author',]
    # fields = ('title', 'content','counted_view', 'published_at',)
    # exclude = ('title', 'content','counted_view', 'published_at',)
# admin.site.register(Post, PostAdmin)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    empty_value_display = ')`:'
    search_fields = ['name',]
    list_filter = ('name',)
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    empty_value_display = ')`:'
    search_fields = ['name',]
    list_filter = ('name',)