# Generated by Django 5.1.3 on 2024-12-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_alter_author_options_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='authors',
            field=models.ManyToManyField(related_name='publications', to='publications.author', verbose_name='Авторы'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='citations',
            field=models.ManyToManyField(blank=True, related_name='publications', to='publications.publication', verbose_name='Цитирования'),
        ),
    ]
