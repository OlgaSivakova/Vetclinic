# Generated by Django 4.1.5 on 2023-02-09 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0038_alter_visitors_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitors',
            name='date',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '31')], default='1', max_length=100, verbose_name='Дата записи'),
        ),
    ]
