# Generated by Django 2.1.7 on 2019-04-17 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_auto_20190402_1703'),
        ('provider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='provider',
            name='apartments',
            field=models.ManyToManyField(to='house.Apartment'),
        ),
    ]
