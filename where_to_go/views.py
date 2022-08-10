from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Image

def main(request):
    places = Place.objects.all()

    context = {
        "places": {
            "type": "FeatureCollection",
            "features": []
        }    
    }
    for place in places:
        context["places"]["features"].append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": []
            },
            "properties": {
                "title": place.title,
                "placeId": "moscow_legends",
                "detailsUrl": "https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/moscow_legends.json"
            }
        })
    return render(request, 'index.html', context)
