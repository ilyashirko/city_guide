import json
import os
import sys

from hashlib import md5

import requests

from city_guide import settings
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from where_to_go.models import Image, Place


def create_location(place_info):
    place, _ = Place.objects.get_or_create(
        title=place_info['title'],
        short_description=place_info['description_short'],
        full_description=place_info['description_long'],
        longitude=float(place_info['coordinates']['lng']),
        latitude=float(place_info['coordinates']['lat']),
    )

    if not place_info['imgs']:
        return place

    for num, url in enumerate(place_info['imgs']):
        download_image(
            num,
            url,
            place,
            os.path.join(settings.MEDIA_PATH, 'images')
        )

    return place, _


def download_image(num, url, place, image_dir):
    response = requests.get(url)
    response.raise_for_status()

    photo = ContentFile(
        response.content,
        name=md5(response.content).hexdigest()
    )
    image, _ = Image.objects.get_or_create(place=place, image=photo, index=num)
    return image, _


class Command(BaseCommand):
    help = "Load places"

    def handle(self, *args, **kwargs):
        if not kwargs['json_path']:
            print('Enter json path, link or directory with jsons...')
            sys.exit()

        entered_path = kwargs['json_path']
        place_info = None

        if os.path.exists(entered_path):
            if '.json' in entered_path:
                try:
                    with open(entered_path, 'r') as file:
                        place_info = json.load(file)
                except json.JSONDecodeError:
                    print('BROKEN JSON')
            else:
                files = os.listdir(entered_path)
                json_files = [file for file in files if '.json' in file]
        else:
            try:
                response = requests.get(entered_path)
                if not response.ok:
                    print('BAD RESPONSE')
                    sys.exit()
                place_info = response.json()
            except json.JSONDecodeError:
                print('BAD CONTENT TYPE')
                sys.exit()
            except requests.exceptions.MissingSchema:
                print('INVALID INPUT')
                sys.exit()

        try:
            if place_info:
                create_location(place_info)
            elif json_files:
                for file in json_files:
                    try:
                        with open(
                            os.path.join(entered_path, file), 'r'
                        ) as place_json:
                            place_info = json.load(place_json)
                            create_location(place_info)
                    except json.JSONDecodeError:
                        print('BROKEN JSON')
            else:
                print('THERE IS NO JSONS HERE')
        except KeyError:
            print('INCORRECT JSON SCHEME')

    def add_arguments(self, parser):
        parser.add_argument(
            '-j',
            '--json_path',
            type=str,
            help=(
                'относительный либо абсолютный путь Json-файла,'
                'url, где content_type == application/json или папка,'
                'которая содержит json-файлы'
            )
        )
        return super().add_arguments(parser)
