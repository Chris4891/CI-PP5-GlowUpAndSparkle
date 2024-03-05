from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings
from store.views.handler404 import Handler404
from django.contrib.auth.models import  Group
urlpatterns = [
    path('kolaradmin/', admin.site.urls),
    path('' , include('store.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = "Glow Up & Sparkle Admin"
admin.site.site_title = "Glow Up & Sparkle Admin Portal"
admin.site.index_title = "Welcome to GLow Up & Sparkle Admin Portal"
admin.site.unregister(Group)
handler404 = Handler404
