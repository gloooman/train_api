from django.db import models

# Create your models here.


class Train(models.Model):
    name = models.CharField('Название тренировки', max_length=128)
    time = models.DateTimeField()
