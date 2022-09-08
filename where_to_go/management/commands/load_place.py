import json
import os
import sys

from hashlib import md5

import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from where_to_go.models import Image, Place


def download_images(place, images_urls):
    if not images_urls:
        return
    for num, url in enumerate(images_urls, start=1):
        response = requests.get(url)
        if not response.ok:
            continue
        photo = ContentFile(
            response.content,
            name=md5(response.content).hexdigest()
        )
        Image.objects.create(
            place=place,
            image=photo,
            index=num,
        )
    return place.images.all()


def extract_places_info(entered_path):
    places_info = list()
    if os.path.isfile(entered_path):
        with open(entered_path, 'r') as file:
            places_info.append(json.load(file))
        return places_info

    for file in os.listdir(entered_path):
        try:
            with open(os.path.join(entered_path, file), 'r') as file_info:
                places_info.append(json.load(file_info))
        except json.JSONDecodeError:
            print(f'BROKEN JSON: "{file}"')
    return places_info


def get_places_info(entered_path):
    if os.path.exists(entered_path):
        places_info = extract_places_info(entered_path)
    else:
        response = requests.get(entered_path)
        response.raise_for_status()
        places_info = (response.json(), )
    return places_info


class Command(BaseCommand):
    help = "Load places"

    def handle(self, *args, **kwargs):
        entered_path = kwargs['json_path']

        try:
            places_info = get_places_info(entered_path)
        except json.JSONDecodeError as error:
            self.stdout.write(self.style.ERROR(error))
            sys.exit()
        except requests.exceptions.MissingSchema as error:
            self.stdout.write(self.style.ERROR('Local file not found.'))
            self.stdout.write(self.style.ERROR(error))
            sys.exit()

        if not places_info:
            return

        for place_info in places_info:
            try:
                place, created = Place.objects.update_or_create(
                    title=place_info['title'],
                    longitude=float(place_info['coordinates']['lng']),
                    latitude=float(place_info['coordinates']['lat']),
                    defaults={
                        'short_description': place_info.get('description_short', ''),
                        'full_description': place_info.get('description_long', '')
                    }
                )
                if created:
                    download_images(place, place_info['imgs'])
            except KeyError as error:
                self.stdout.write(self.style.ERROR(error))
            except Place.MultipleObjectsReturned as error:
                self.stdout.write(self.style.ERROR(f'[{place_info["title"]}]: {error}'))

    def add_arguments(self, parser):
        parser.add_argument(
            '-j',
            '--json_path',
            type=str,
            help=(
                'относительный либо абсолютный путь Json-файла,'
                'url, где content_type == application/json или папка,'
                'которая содержит json-файлы'
            ),
            required=True
        )
        return super().add_arguments(parser)