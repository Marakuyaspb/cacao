from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin

from django.urls import path, include

from cacao import views
from cacao import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cacao.urls')),
    #url(r'^telegrambot/', include('telegrambot.urls', namespace="telegrambot")),
]


urlpatterns += static(
    settings.STATIC_URL, 
    document_root=settings.STATIC_ROOT
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)