from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from where_to_go.views import main_page, place_via_id

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('places/<int:place_id>', place_via_id),
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATICFILES_DIRS
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
