from django.db import models
from django.contrib.auth import get_user_model

class Street(models.Model):
    name = models.CharField(max_length=50)


class House(models.Model):
    name = models.CharField(max_length=20)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)


class Apartment(models.Model):
    name = models.CharField(max_length=20)
    license = models.CharField(max_length=20)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
