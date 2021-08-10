from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # Custom app urls
    path('', include('general.urls')),
    path('communities/', include('communities.urls')),
    path('events/', include('events.urls')),
    path('outputs/', include('outputs.urls')),

    # Include Django admin urls
    path('dashboard/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
