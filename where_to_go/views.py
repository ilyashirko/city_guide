# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

from .models import Place


def make_geojson_feature(request, place):
    return {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.longitude, place.latitude]
        },
        "properties": {
            "title": place.title,
            "detailsUrl": f'{settings.PLACE_API_URL}/{place.id}'
        }
    }


def render_main_page(request):
    places = Place.objects.all()
    features = [make_geojson_feature(request, place) for place in places]
    context = {
        'all_places': {
            'type': 'FeatureCollection',
            'features': features
        }
    }
    return render(request, 'index.html', context)


def get_place_dict_via_id(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    images_urls = [image.image.url for image in place.images.all()]

    details = {
        'title': place.title,
        'imgs': images_urls,
        'description_short': place.short_description,
        'description_long': place.full_description,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }
    return JsonResponse(details, json_dumps_params={'ensure_ascii': False})
