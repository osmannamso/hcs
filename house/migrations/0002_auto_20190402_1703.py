# Generated by Django 2.1.7 on 2019-04-02 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apartment',
            options={'verbose_name': 'Квартира', 'verbose_name_plural': 'Квартиры'},
        ),
        migrations.AlterModelOptions(
            name='house',
            options={'verbose_name': 'Дом', 'verbose_name_plural': 'Дома'},
        ),
        migrations.AlterModelOptions(
            name='street',
            options={'verbose_name': 'Улица', 'verbose_name_plural': 'Улицы'},
        ),
    ]
