# Generated by Django 4.2 on 2023-09-02 13:21

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import mptt_blog_api.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('url', models.TextField(verbose_name='Url адрес')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('author', models.ForeignKey(default=mptt_blog_api.models.category_author_default, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('parent', mptt.fields.TreeForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='mptt_blog_api.categoryblog', verbose_name='Родительская категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='PostBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('text', ckeditor.fields.RichTextField(verbose_name='Текст')),
                ('is_private', models.BooleanField(default=False, verbose_name='Вижу только я')),
                ('like_count', models.BigIntegerField(default='0', verbose_name='Количество лайков')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('author', models.ForeignKey(default=mptt_blog_api.models.category_author_default_post, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('category', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_post', to='mptt_blog_api.categoryblog', verbose_name='Категория')),
                ('favourites', models.ManyToManyField(blank=True, default=None, related_name='favourites_post', to=settings.AUTH_USER_MODEL, verbose_name='В избранных')),
                ('likes', models.ManyToManyField(blank=True, default=None, related_name='likes_post', to=settings.AUTH_USER_MODEL, verbose_name='Поставили лайк')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
        migrations.CreateModel(
            name='CommentsPostBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', ckeditor.fields.RichTextField(max_length=400, verbose_name='Текст')),
                ('like_count', models.BigIntegerField(default='0', verbose_name='Количество лайков')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('author', models.ForeignKey(default=mptt_blog_api.models.category_author_default, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('likes', models.ManyToManyField(blank=True, default=None, related_name='likes_comment', to=settings.AUTH_USER_MODEL, verbose_name='Поставили лайк')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='mptt_blog_api.postblog', verbose_name='Статья')),
            ],
        ),
    ]
