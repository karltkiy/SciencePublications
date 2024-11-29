from django.urls import path
from . import views

urlpatterns = [
    path('', views.publication_list, name='publication_list'),
    path('category/<int:pk>/', views.publication_list,
         name='publication_list_by_category'),
    path('publication/<int:pk>/', views.publication_detail,
         name='publication_detail'),
]
