# Generated by Django 3.2.3 on 2021-07-31 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0004_comments_is_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='is_published',
        ),
    ]