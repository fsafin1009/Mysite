from django.contrib import admin

from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'is_published', 'data_published')
    list_display_links = ('id', 'title')

admin.site.register(Article, ArticleAdmin)
