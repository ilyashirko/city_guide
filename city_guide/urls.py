from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from where_to_go.views import main_page, place_via_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('places/<int:place_id>', place_via_id),
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
