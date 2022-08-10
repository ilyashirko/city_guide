import os
from django.db import models

from city_guide.settings import IMAGES_PATH

class Place(models.Model):
    title = models.CharField('Название', max_length=100)
    short_description = models.TextField('Короткое описание')
    full_description = models.TextField('Полное описание')
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return f'{self.title} [{self.longitude}, {self.latitude}]'

class Image(models.Model):
    place = models.ForeignKey(
        'Place',
        verbose_name='Локация',
        related_name='place',
        on_delete=models.CASCADE
    )
    index = models.SmallIntegerField('Порядковый номер (UNIQUE ONLY)')
    image = models.ImageField('Изображение', upload_to=IMAGES_PATH)
    