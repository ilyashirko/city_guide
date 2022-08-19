from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from where_to_go.models import Image, Place


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ("preview", )
    fields = ('image', 'preview', 'index')
    def preview(self, obj):
        return format_html(
            f'<img src="{obj.image.url}" '
            f'height=200 />'
    )


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
