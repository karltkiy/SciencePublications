from django.contrib import admin
from .models import Category, Edition, Issue, Author, Publication


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('edition', 'number', 'date')
    list_filter = ('edition', 'date')
    search_fields = ('number',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'issue', 'created_at')
    list_filter = ('category', 'issue', 'created_at')
    search_fields = ('title', 'abstract', 'keywords')
    filter_horizontal = ('authors', 'citations')
