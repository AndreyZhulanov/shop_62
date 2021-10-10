from django.contrib import admin

from .models import PostModel, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'author', 'title', 'text', 'image', 'publish_date', 'slug', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'publish_date')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


# Register your models here.
admin.site.register(PostModel, PostAdmin)
admin.site.register(Category, CategoryAdmin)
