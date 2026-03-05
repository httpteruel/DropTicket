from django.contrib import admin
from django.urls import path
from core.views import home
from django.conf import settings
from django.conf.urls.static import static
from core.views import home, detalhe_evento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('evento/<int:evento_id>/', detalhe_evento, name='detalhe_evento'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)