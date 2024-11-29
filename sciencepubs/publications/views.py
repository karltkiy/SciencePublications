from django.shortcuts import render, get_object_or_404
from .models import Publication, Category, Edition


def publication_list(request, pk=None):
    if pk:
        category = get_object_or_404(Category, pk=pk)
        publications = Publication.objects.filter(
            category=category).order_by('-created_at')
    else:
        publications = Publication.objects.all().order_by('-created_at')
    categories = Category.objects.all()
    editions = Edition.objects.all()
    context = {
        'publications': publications,
        'categories': categories,
        'editions': editions,
    }
    if pk:
        context['current_category'] = category
    return render(request, 'publications/publication_list.html', context)


def publication_detail(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    return render(request, 'publications/publication_detail.html', {
        'publication': publication
    })
