from django.db import models
from tinymce.models import HTMLField

from city_guide.settings import IMAGES_PATH


class Place(models.Model):
    title = models.CharField('Название', max_length=100)
    short_description = models.TextField('Короткое описание', blank=True)
    full_description = HTMLField('Полное описание', blank=True)
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return f'{self.title} [{self.longitude}, {self.latitude}]'

    class Meta:
        ordering = ['id', ]


class Image(models.Model):
    place = models.ForeignKey(
        'Place',
        verbose_name='Локация',
        related_name='images',
        on_delete=models.CASCADE
    )
    index = models.SmallIntegerField(
        'Порядковый номер (UNIQUE ONLY)',
        default=0
    )
    image = models.ImageField('Изображение', upload_to=IMAGES_PATH)

    class Meta:
        ordering = ['index', ]

    def __str__(self):
        return f'{self.place}_{self.index}'
