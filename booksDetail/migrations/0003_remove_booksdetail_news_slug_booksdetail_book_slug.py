# Generated by Django 5.0.6 on 2024-06-19 10:19

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booksDetail', '0002_booksdetail_news_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booksdetail',
            name='news_slug',
        ),
        migrations.AddField(
            model_name='booksdetail',
            name='book_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='book_title', unique=True),
        ),
    ]
