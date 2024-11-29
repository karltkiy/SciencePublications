from django.db import models

# Create your models here.
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Edition(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Issue(models.Model):
    edition = models.ForeignKey(Edition, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.edition.name} - Issue {self.number} ({self.date})"


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(blank=True)
    affiliation = models.TextField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Publication(models.Model):
    title = models.CharField(max_length=500)
    authors = models.ManyToManyField(Author)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    pages = models.CharField(max_length=50)  # e.g., "123-145"
    doi = models.CharField(max_length=50, default='10.1000/123')
    keywords = models.CharField(max_length=500)
    abstract = models.TextField()
    text = models.TextField()
    citations = models.ManyToManyField('self', symmetrical=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
