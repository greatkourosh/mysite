from django.contrib import admin

from .models import Contact, Newsletter

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    empty_value_display = ')`:'
    list_display = ('name', 'email', 'created_at',)
    list_filter = ('email',)
    ordering = ['-created_at']
    search_fields = ['name', 'message']
    # fields = ('title', 'content','counted_view', 'published_at',)
    # exclude = ('title', 'content','counted_view', 'published_at',)

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    # date_hierarchy = 'created_at'
    empty_value_display = ')`:'
    list_display = ('email',)
    list_filter = ('email',)
    # ordering = ['-created_at']
    search_fields = ['email',]
    # fields = ('title', 'content','counted_view', 'published_at',)
    # exclude = ('title', 'content','counted_view', 'published_at',)