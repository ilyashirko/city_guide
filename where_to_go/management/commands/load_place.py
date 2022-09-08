import json
import os
import sys

from hashlib import md5

import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from where_to_go.models import Image, Place


def create_location(place_info):
    place, _ = Place.objects.update_or_create(
        title=place_info['title'],
        longitude=float(place_info['coordinates']['lng']),
        latitude=float(place_info['coordinates']['lat']),
        defaults={
            'short_description': place_info.get('description_short', ''),
            'full_description': place_info.get('description_long', '')
        }
    )
    return place, _


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


def get_places_info(entered_path):
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


class Command(BaseCommand):
    help = "Load places"

    def handle(self, *args, **kwargs):
        if not kwargs['json_path']:
            print('Enter json path, link or directory with jsons...')
            sys.exit()

        entered_path = kwargs['json_path']

        if os.path.exists(entered_path):
            try:
                places_info = get_places_info(entered_path)
            except json.JSONDecodeError:
                print('BROKEN JSON')
        else:
            try:
                response = requests.get(entered_path)
                if not response.ok:
                    print('BAD RESPONSE')
                    sys.exit()
                places_info = (response.json(), )
            except json.JSONDecodeError:
                print('BAD CONTENT TYPE')
                sys.exit()
            except requests.exceptions.MissingSchema:
                print('INVALID INPUT')
                sys.exit()

        if not places_info:
            return

        for place_info in places_info:
            try:
                place, created = create_location(place_info)
                if not created:
                    continue
                download_images(place, place_info['imgs'])
            except KeyError:
                print('INCORRECT JSON SCHEME')
            except Place.MultipleObjectsReturned:
                continue

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
