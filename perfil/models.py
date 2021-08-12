from django.db import models

from perfil.managers import PerfilManager
# Create your models here.


class Perfil(models.Model):
    idade = models.IntegerField()
    altura = models.IntegerField()
    massa = models.IntegerField()

    objects = PerfilManager()

    class Meta:
        verbose_name_plural = 'Perfis'
