# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

Tipo_Choices = (
    ('AC', 'Activo'),
    ('DC', 'Desactivo'),
)

Default_Tipo = 'AC'

class Licencia(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    tipo = models.CharField(max_length=2,choices=Tipo_Choices,default=Default_Tipo)
    def __str__(self):
        return self.name