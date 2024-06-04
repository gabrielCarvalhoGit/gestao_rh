from django.urls import path
from .views import (hora_extra_list, hora_extra_create, hora_extra_edit, hora_extra_delete)


urlpatterns = [
    path('', hora_extra_list, name='hora-extra-list'),
    path('create/', hora_extra_create, name='hora-extra-create'),
    path('edit/<int:id>', hora_extra_edit, name='hora-extra-edit'),
    path('delete/<int:id>', hora_extra_delete, name='hora-extra-delete'),
]