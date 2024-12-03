from django.db import models

# Create your models here.


class CommonModel(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Category(CommonModel):
    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"


class Edition(CommonModel):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Категория', related_name='editions')

    class Meta:
        verbose_name = "издание"
        verbose_name_plural = "Издания"


class Issue(models.Model):
    edition = models.ForeignKey(
        Edition, on_delete=models.CASCADE, verbose_name='Издание', related_name='issues')
    number = models.CharField(max_length=50, verbose_name='Номер')
    date = models.DateField(verbose_name='Дата')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f"{self.edition.name} - Issue {self.number} ({self.date})"

    class Meta:
        verbose_name = "выпуск"
        verbose_name_plural = "Выпуски"


class Author(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    email = models.EmailField(blank=True, verbose_name='Эл. почта')
    affiliation = models.TextField(verbose_name='Должность')
    bio = models.TextField(blank=True, verbose_name='Биография')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "автор"
        verbose_name_plural = "Авторы"


class ExternalPublication(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    authors = models.CharField(max_length=500, verbose_name='Авторы')
    source = models.CharField(max_length=500, verbose_name='Источник')
    year = models.IntegerField(verbose_name='Год')
    url = models.URLField(blank=True, verbose_name='URL-адрес')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "внешний источник"
        verbose_name_plural = "Внешние источники"


class Publication(models.Model):
    title = models.CharField(max_length=500, verbose_name='Заголовок')
    authors = models.ManyToManyField(
        Author, verbose_name='Авторы', related_name='publications')
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE,
                              verbose_name='Выпуск', related_name='publications')
    pages = models.CharField(
        max_length=50, verbose_name='Страницы')  # e.g., "123-145"
    doi = models.CharField(
        max_length=50, default='10.1000/123', verbose_name='DOI')
    keywords = models.CharField(max_length=500, verbose_name='Ключевые слова')
    abstract = models.TextField(verbose_name='Аннотация')
    text = models.TextField(verbose_name='Текст')
    citations = models.ManyToManyField(
        'self', symmetrical=False, blank=True, verbose_name='Цитирования', related_name='publications')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Дата изменения')
    external_citations = models.ManyToManyField(
        ExternalPublication, blank=True, related_name='cited_by', verbose_name='Внешние источники')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"
        ordering = ('-created_at',)
