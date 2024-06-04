from django.urls import path
from .views import (departamento_list, departamento_create, departamento_edit, departamento_delete)


urlpatterns = [
    path('', departamento_list, name='departamento-list'),
    path('create', departamento_create, name='departamento-create'),
    path('edit/<int:id>', departamento_edit, name='departamento-edit'),
    path('delete/<int:id>', departamento_delete, name='departamento-delete'),
]