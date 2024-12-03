from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
# from django.http import JsonResponse
# from django.views.decorators.http import require_GET
from .models import Publication, Author, Category, Edition, Issue
from .utils import generate_citation, generate_external_citation


class PublicationListView(ListView):
    model = Publication
    template_name = 'publications/publication_list.html'
    context_object_name = 'publications'
    paginate_by = 10

    def get_queryset(self):
        queryset = Publication.objects.all()

        # Filter by authors
        authors = self.request.GET.getlist('author')
        if authors:
            queryset = queryset.filter(authors__id__in=authors)

        # Filter by categories
        categories = self.request.GET.getlist('category')
        if categories:
            queryset = queryset.filter(
                issue__edition__category__id__in=categories)

        # Filter by editions
        editions = self.request.GET.getlist('edition')
        if editions:
            queryset = queryset.filter(issue__edition__id__in=editions)

        # Filter by issues
        issues = self.request.GET.getlist('issue')
        if issues:
            queryset = queryset.filter(issue__id__in=issues)

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Define filter groups
        context['filter_groups'] = [
            {
                'id': 'authors',
                'title': 'Authors',
                'param': 'author',
                'items': Author.objects.all()
            },
            {
                'id': 'categories',
                'title': 'Categories',
                'param': 'category',
                'items': Category.objects.all()
            },
            {
                'id': 'editions',
                'title': 'Editions',
                'param': 'edition',
                'items': Edition.objects.all()
            },
            {
                'id': 'issues',
                'title': 'Issues',
                'param': 'issue',
                'items': Issue.objects.all()
            }
        ]
        return context


def get_cited_publications(publication_id):
    publication = get_object_or_404(Publication, pk=publication_id)

    # Get internal citations
    cited_publications = []
    for cited_pub in publication.citations.all():
        cited_publications.append({
            'publication': cited_pub,
            'citation': generate_citation(cited_pub, 'gost'),
            'type': 'internal'
        })

    # Get external citations
    for external_pub in publication.external_citations.all():
        cited_publications.append({
            'publication': external_pub,
            'citation': generate_external_citation(external_pub, 'gost'),
            'type': 'external'
        })

    # Sort citations by year
    cited_publications.sort(
        key=lambda x: x['publication'].issue.date.year if x['type'] == 'internal'
        else x['publication'].year,
        reverse=True
    )

    return cited_publications


def publication_detail(request, publication_id):
    publication = get_object_or_404(Publication, pk=publication_id)

    # Generate citations in different formats
    citations = {
        'gost': generate_citation(publication, 'gost'),
        'apa': generate_citation(publication, 'apa'),
        'mla': generate_citation(publication, 'mla'),
    }

    context = {
        'publication': publication,
        'citations': citations,
        'cited_publications': get_cited_publications(publication_id),
    }

    return render(request, 'publications/publication_detail.html', context)


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'publications/author_detail.html', {
        'author': author
    })


# @require_GET
# def format_citations(request):
#     style = request.GET.get('style', 'gost')

#     # Get the current publication's references
#     cited_publications = get_cited_publications(
#         request.GET.get('publication_id'))

#     # Format citations according to the requested style
#     formatted_citations = []
#     for pub in cited_publications:
#         if style == 'apa':
#             citation = generate_citation(pub, 'apa')
#         elif style == 'mla':
#             citation = generate_citation(pub, 'mla')
#         else:
#             citation = generate_citation(pub, 'gost')  # default to GOST

#         formatted_citations.append(citation)

#     return JsonResponse({
#         'citations': formatted_citations
#     })
