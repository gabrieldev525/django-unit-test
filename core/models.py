# django imports
from django.db import models

# local imports
from .constants import STATUS_CREATION
from .constants import NOT_CREATED



class Register(models.Model):
    name = models.CharField('name', max_length=255, null=True)
    desc = models.TextField('Descrição', blank=True, null=True)
    target = models.TextField('Intervalo de ativos')
    status = models.IntegerField(
        'Status', choices=STATUS_CREATION, default=NOT_CREATED)
