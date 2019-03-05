from django.db import models
from django.contrib.auth import get_user_model

class Street(models.Model):
    class Meta:
        verbose_name_plural = 'Улицы'
        verbose_name = 'Улица'
    name = models.CharField(max_length=50)


class House(models.Model):
    class Meta:
        verbose_name_plural = 'Дома'
        verbose_name = 'Дом'
    name = models.CharField(max_length=20)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)


class Apartment(models.Model):
    class Meta:
        verbose_name_plural = 'Квартиры'
        verbose_name = 'Квартира'
    name = models.CharField(max_length=20)
    license = models.CharField(max_length=20)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
