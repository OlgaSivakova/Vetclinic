# Generated by Django 4.1.5 on 2023-02-02 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0022_alter_visitors_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitors',
            name='date',
            field=models.DateField(blank=True, null=True, unique=True, verbose_name='Дата записи: (yyyy-mm-dd)'),
        ),
    ]
