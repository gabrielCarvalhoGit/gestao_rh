from django.urls import path
from .views import (funcionario_list, funcionario_edit, funcionario_delete, funcionario_create)


urlpatterns = [
    path('', funcionario_list, name='funcionario-list'),
    path('create', funcionario_create, name=('funcionario-create')),
    path('edit/<int:id>', funcionario_edit, name='funcionario-edit'),
    path('delete/<int:id>', funcionario_delete, name='funcionario-delete'),
]