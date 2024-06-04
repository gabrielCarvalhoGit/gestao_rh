from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.core.urls")),
    path('empresa/', include("apps.empresas.urls")),
    path('funcionarios/', include("apps.funcionarios.urls")),
    path('departamentos/', include("apps.departamentos.urls")),
    path('documentos/', include("apps.documentos.urls")),
    path('horas-extras/', include("apps.registro_horas_extras.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)