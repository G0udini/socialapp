from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar


urlpatterns = [
    path("account/", include("account.urls")),
    path("admin/", admin.site.urls),
    path("social-auth/", include("social_django.urls", namespace="social")),
    path("images/", include("images.urls", namespace="images")),
    path("__debug__/", include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
