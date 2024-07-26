from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static  # for serving images, we are importing this.
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blogapp.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
