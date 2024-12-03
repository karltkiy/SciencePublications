from django.urls import path
from . import views

urlpatterns = [
    path('', views.PublicationListView.as_view(), name='publication_list'),
    path('publication/<int:publication_id>/', views.publication_detail,
         name='publication_detail'),
    path('author/<int:author_id>/', views.author_detail,
         name='author_detail'),
#     path('api/format-citations/',
#          views.format_citations, name='format_citations'),
]
