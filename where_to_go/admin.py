from adminsortable2.admin import SortableAdminBase, SortableStackedInline
from django.contrib import admin
from django.utils.html import format_html

from where_to_go.models import Image, Place


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ("preview", )
    fields = ['id', 'image', 'preview', ]
    extra = 0

    def preview(self, obj):
        return format_html(
            f'<img src="{obj.image.url}" '
            f'height=200 />'
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = (
        'title',
        'short_description',
        'longitude',
        'latitude'
    )
    inlines = [
        ImageInline,
    ]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('place', )
    list_display = ('place', 'index', 'image')
    list_filter = ('place', )
