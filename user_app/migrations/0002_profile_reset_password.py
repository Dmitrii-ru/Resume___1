# Generated by Django 4.2 on 2023-07-29 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='reset_password',
            field=models.BooleanField(default=False),
        ),
    ]
