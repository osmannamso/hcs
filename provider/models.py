from django.db import models
from django.contrib.auth.models import User
from house.models import Apartment


class Provider(models.Model):
    class Meta:
        verbose_name_plural = 'Провайдеры'
        verbose_name = 'Провайдер'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    provision = models.CharField(max_length=25)
    apartments = models.ManyToManyField(Apartment)

    def __str__(self):
        return self.name + self.provision


class Payment(models.Model):
    class Meta:
        verbose_name_plural = 'Предметы для оплаты'
        verbose_name = 'Предмет оплаты'
    name = models.CharField(max_length=25)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + self.provider.name + self.provider.provision


class Check(models.Model):
    class Meta:
        verbose_name = 'Квитанция'
        verbose_name_plural = 'Квитанции'
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    price = models.IntegerField()
