# Generated by Django 4.1.5 on 2023-02-03 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0031_alter_comments_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Имя')),
                ('surname', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('content', models.TextField(null=True, verbose_name='Специализация')),
                ('exp', models.CharField(max_length=250, verbose_name='Опят работы')),
            ],
        ),
    ]