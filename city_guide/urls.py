from django.contrib import admin
from django.urls import path
from where_to_go  import views
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main)
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
