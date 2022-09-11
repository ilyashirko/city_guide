from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from where_to_go.views import get_place_dict_via_id, render_main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_main_page),
    path('places/<int:place_id>/', get_place_dict_via_id, name='places_api'),
    path('tinymce/', include('tinymce.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
