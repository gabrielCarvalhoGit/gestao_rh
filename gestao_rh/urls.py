from django.contrib import admin
from django.conf import settings
from rest_framework import routers
from django.urls import path, include
from django.conf.urls.static import static

from apps.core import views
from apps.funcionarios.api.views import FuncionarioViewSet
from apps.registro_horas_extras.api.views import RegistroHoraExtraViewSet


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'api/funcionarios', FuncionarioViewSet)
router.register(r'api/banco-horas', RegistroHoraExtraViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.core.urls")),
    path('empresa/', include("apps.empresas.urls")),
    path('funcionarios/', include("apps.funcionarios.urls")),
    path('departamentos/', include("apps.departamentos.urls")),
    path('documentos/', include("apps.documentos.urls")),
    path('horas-extras/', include("apps.registro_horas_extras.urls")),
    path('accounts/', include("django.contrib.auth.urls")),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)