# Generated by Django 4.1.5 on 2023-02-02 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0030_remove_comments_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='content',
            field=models.TextField(null=True, verbose_name='Ваш отзыв'),
        ),
    ]
