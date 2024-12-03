from django.contrib import admin
from .models import Category, Edition, Issue, Author, Publication, ExternalPublication


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Edition)
class EditionAdmin(admin.ModelAdmin):
    list_display = ('name', 'category',)
    search_fields = ('name', 'category',)


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
    list_display = ('title', 'issue', 'created_at')
    list_filter = ('issue', 'created_at')
    search_fields = ('title', 'abstract', 'keywords')
    filter_horizontal = ('authors', 'citations')


@admin.register(ExternalPublication)
class ExternalPublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'year', 'source')
    search_fields = ('title', 'authors', 'source')
    list_filter = ('year',)


admin.site.empty_value_display = 'Не задано'
