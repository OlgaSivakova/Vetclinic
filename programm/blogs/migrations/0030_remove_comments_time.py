# Generated by Django 4.1.5 on 2023-02-02 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0029_comments_alter_visitors_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='time',
        ),
    ]
