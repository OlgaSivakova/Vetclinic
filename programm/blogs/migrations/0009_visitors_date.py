# Generated by Django 4.1.5 on 2023-01-29 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_alter_visitors_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitors',
            name='date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата записи'),
        ),
    ]
