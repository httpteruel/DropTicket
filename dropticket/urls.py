from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import EventoListView, EventoDetailView, EventoCreateView, EventoUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', EventoListView.as_view(), name='evento_list'),
    
    path('evento/<slug:slug>/', EventoDetailView.as_view(), name='evento_detail'),
    
    path('evento/novo/', EventoCreateView.as_view(), name='evento_create'),
    path('evento/<slug:slug>/editar/', EventoUpdateView.as_view(), name='evento_update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
