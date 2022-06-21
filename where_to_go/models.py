from django.db import models

class Place(models.Model):
    title = models.CharField('Название', max_length=100)
    short_description = models.TextField('Короткое описание')
    full_description = models.TextField('Полное описание')
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')
