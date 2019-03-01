from django.db import models
from django.contrib.auth import get_user_model


class Role(models.Model):
    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'

    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name


class User(models.Model):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
