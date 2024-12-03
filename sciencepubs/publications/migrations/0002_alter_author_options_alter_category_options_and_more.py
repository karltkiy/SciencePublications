# Generated by Django 5.1.3 on 2024-12-01 10:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='edition',
            options={'verbose_name': 'издание', 'verbose_name_plural': 'Издания'},
        ),
        migrations.AlterModelOptions(
            name='issue',
            options={'verbose_name': 'выпуск', 'verbose_name_plural': 'Выпуски'},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'ordering': ('-created_at',), 'verbose_name': 'публикация', 'verbose_name_plural': 'Публикации'},
        ),
        migrations.AlterField(
            model_name='author',
            name='affiliation',
            field=models.TextField(verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='author',
            name='bio',
            field=models.TextField(blank=True, verbose_name='Биография'),
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Эл. почта'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='edition',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='publications.edition', verbose_name='Издание'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='number',
            field=models.CharField(max_length=50, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='abstract',
            field=models.TextField(verbose_name='Аннотация'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='authors',
            field=models.ManyToManyField(to='publications.author', verbose_name='Авторы'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='publications.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='citations',
            field=models.ManyToManyField(blank=True, to='publications.publication', verbose_name='Цитирования'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='doi',
            field=models.CharField(default='10.1000/123', max_length=50, verbose_name='DOI'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='issue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='publications.issue', verbose_name='Выпуск'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='keywords',
            field=models.CharField(max_length=500, verbose_name='Ключевые слова'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='pages',
            field=models.CharField(max_length=50, verbose_name='Страницы'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата изменения'),
        ),
    ]