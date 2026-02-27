from django.contrib import admin
from django.urls import path
from core.views import home # Importa sua nova view
from django.conf import settings
from django.conf.urls.static import static
from core.views import home, detalhe_evento  # Adicione o detalhe_evento aqui!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'), # Página inicial
    path('evento/<int:evento_id>/', detalhe_evento, name='detalhe_evento'), # Nova rota
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)