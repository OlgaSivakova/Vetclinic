# Generated by Django 4.1.5 on 2023-01-30 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_alter_visitors_optionvar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor01',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
