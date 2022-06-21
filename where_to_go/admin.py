from django.contrib import admin

from where_to_go.models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'short_description',
        'longitude',
        'latitude'
    )
