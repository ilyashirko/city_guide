from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from where_to_go.views import render_main_page, get_place_dict_via_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_main_page),
    path(f'{settings.PLACE_API_URL}/<int:place_id>', get_place_dict_via_id),
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=(
        settings.STATICFILES_DIRS
        if settings.DEBUG
        else settings.STATIC_ROOT
    )
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
