from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
