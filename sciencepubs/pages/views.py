from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'pages/about.html'


class LegalView(TemplateView):
    template_name = 'pages/legal.html'


class ContactView(TemplateView):
    template_name = 'pages/contact.html'
