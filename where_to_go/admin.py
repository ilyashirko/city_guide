from django.contrib import admin

from where_to_go.models import Image, Place


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'short_description',
        'longitude',
        'latitude'
    )
    inlines = (ImageInline, )


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place', )
    list_display = ('place', 'index', 'image')
    list_filter = ('place', )
