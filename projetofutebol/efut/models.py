from django.db import models


class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
