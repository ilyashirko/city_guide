from django.db import models

class Place(models.Model):
    title = models.CharField('Название', max_length=100)
    short_description = models.TextField('Короткое описание')
    full_description = models.TextField('Полное описание')
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

class Image(models.Model):
    place = models.ForeignKey(
        'Place',
        verbose_name='Локация',
        related_name='place',
        on_delete=models.CASCADE
    )
    image = models.ImageField('Изображение')