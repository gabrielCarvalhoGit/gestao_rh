from django.urls import path
from .views import DocumentoCreate


urlpatterns = [
    path('create/<int:funcionario_id>/', DocumentoCreate.as_view(), name='documento-create')
]