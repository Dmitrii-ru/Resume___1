# Generated by Django 4.2 on 2023-08-30 10:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_alter_uniqueip_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uniqueip',
            options={'verbose_name': 'Посетитель', 'verbose_name_plural': 'Посетители 0'},
        ),
        migrations.AlterField(
            model_name='aboutme',
            name='text',
            field=ckeditor.fields.RichTextField(max_length=4000, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='uniqueip',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
