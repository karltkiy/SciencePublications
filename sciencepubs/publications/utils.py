from citeproc import (Citation, CitationItem, CitationStylesBibliography,
                      CitationStylesStyle, formatter)
from citeproc.source.json import CiteProcJSON
from citeproc_styles import get_style_filepath

# Map of supported citation styles
STYLES = {
    'gost': 'gost-r-7-0-5-2008',
    'apa': 'apa',
    'mla': 'modern-language-association'
}


def create_citation_item(publication):
    """Convert Publication model to citation item format"""
    authors = [{
        'family': author.name.split()[-1],
        'given': ' '.join(author.name.split()[:-1])
    } for author in publication.authors.all()]

    return {
        'id': str(publication.id),
        'type': 'article-journal',
        'title': publication.title,
        'author': authors,
        'container-title': publication.issue.edition.name,
        'volume': publication.issue.number,
        'page': publication.pages,
        'issued': {'date-parts': [[publication.issue.date.year]]},
        'DOI': publication.doi
    }


def generate_citation(publication, style_str='gost'):
    """Generate citation in specified format"""
    # Create citation item
    citation_item = create_citation_item(publication)
    bib_source = CiteProcJSON([citation_item])

    # Load citation style
    style = CitationStylesStyle(get_style_filepath(
        STYLES.get(style_str, 'gost-r-7-0-5-2008')))

    # Create bibliography
    bibliography = CitationStylesBibliography(
        style, bib_source, formatter.html)

    # Generate citation
    bibliography.register(Citation([CitationItem(str(publication.id))]))

    result = ''.join(bibliography.bibliography()[0])
    if style_str == 'gost':
        return result[3:-1]
    return result


def create_external_citation_item(external_publication):
    """Convert ExternalPublication to citation item format"""
    # Parse authors string into list of authors
    authors = [{
        'family': author.strip().split()[-1],
        'given': ' '.join(author.strip().split()[:-1])
    } for author in external_publication.authors.split(',')]

    return {
        'id': f'external-{external_publication.id}',
        'type': 'article-journal',
        'title': external_publication.title,
        'author': authors,
        'container-title': external_publication.source,
        'issued': {'date-parts': [[external_publication.year]]},
        'URL': external_publication.url if external_publication.url else None
    }


def generate_external_citation(external_publication, style='gost'):
    """Generate citation for external publication"""
    citation_item = create_external_citation_item(external_publication)
    return generate_citation_from_item(citation_item, style)


def generate_citation_from_item(citation_item, style='gost'):
    """Generate citation from citation item"""
    bib_source = CiteProcJSON([citation_item])
    style = CitationStylesStyle(get_style_filepath(
        STYLES.get(style, 'gost-r-7-0-5-2008')))
    bibliography = CitationStylesBibliography(
        style, bib_source, formatter.html)
    bibliography.register(citation_item)

    return ''.join(bibliography.bibliography()[0])
