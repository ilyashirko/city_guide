# -*- coding: utf-8 -*-

from urllib.parse import urljoin

from city_guide import settings
from django.http import JsonResponse
from django.shortcuts import render

from .models import Place


def main_page(request):
    places = Place.objects.all()
    context = {
        "all_places": {
            "type": "FeatureCollection",
            "features": []
        }
    }
    for place in places:
        context["all_places"]["features"].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": "moscow_legends",
                "detailsUrl": f'http://127.0.0.1:8000/places/{place.id}'
            }
        })
    return render(request, 'index.html', context)


def place(request, place_id=None):
    place = Place.objects.get(id=place_id)
    images_paths = [str(image.image) for image in place.place.all()]
    images_urls = [
        urljoin(request.get_host(), f'{settings.MEDIA_URL}{image_path}')
        for image_path in images_paths
    ]

    detailes = {
            "title": place.title,
            "imgs": images_urls,
            "description_short": place.short_description,
            "description_long": place.full_description,
            "coordinates": {
                "lng": place.longitude,
                "lat": place.latitude
            }
        }
    return JsonResponse(detailes)
