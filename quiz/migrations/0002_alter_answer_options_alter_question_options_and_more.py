# Generated by Django 4.2 on 2023-07-14 14:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы '},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'Тест', 'verbose_name_plural': 'Тесты'},
        ),
        migrations.AlterField(
            model_name='quiz',
            name='is_completed',
            field=models.ManyToManyField(blank=True, related_name='quiz_completed', to=settings.AUTH_USER_MODEL, verbose_name='Прошли тест'),
        ),
    ]
