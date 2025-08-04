from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/tattoo-artists/', include('apps.tattoo_artist.urls')),
    path('api/users/', include('apps.users.urls')),
    path('api/tattoo-styles/', include('apps.tattoo_styles.urls')),
    path('api/tattoo-techniques/', include('apps.tattoo_techniques.urls')),
    path('api/tattoo-machine-types/', include('apps.tattoo_machine_types.urls')),
    path('api/tattoo-body-parts/', include('apps.tattoo_body_parts.urls')),
    path('api/tattoo-artworks/', include('apps.tattoo_artworks.urls')),  # ✅ corrigido
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)