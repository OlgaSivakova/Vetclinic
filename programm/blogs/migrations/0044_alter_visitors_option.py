# Generated by Django 4.1.5 on 2023-02-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0043_alter_visitors_email_alter_visitors_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitors',
            name='option',
            field=models.CharField(choices=[('Собака', 'Собака'), ('Кот', 'Кот'), ('Грызун', 'Грызуны'), ('Птица', 'Птица')], default='Выбрать питомца', max_length=100, verbose_name='Вид питомца'),
        ),
    ]
