from django.urls import path
from .views import (add_empresa, edit_empresa)

urlpatterns = [
    path('createempresa/', add_empresa, name='create-empresa'),
    path('edit/<int:id>', edit_empresa, name='edit-empresa'),
]