# Generated by Django 4.1.5 on 2023-02-05 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0035_alter_visitors_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitors',
            name='time',
            field=models.CharField(default='00:00', max_length=5, null=True, unique=True, verbose_name='Время записи'),
        ),
    ]
