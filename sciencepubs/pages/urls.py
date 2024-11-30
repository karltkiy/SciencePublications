from django.urls import path
from .views import AboutView, LegalView, ContactView

app_name = 'pages'

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('legal/', LegalView.as_view(), name='legal'),
    path('contact/', ContactView.as_view(), name='contact'),
]
