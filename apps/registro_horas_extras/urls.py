from django.urls import path
from .views import (hora_extra_list, 
                    hora_extra_create, 
                    hora_extra_edit, 
                    hora_extra_edit_funcionario, 
                    hora_extra_delete,
                    hora_extra_utilizada)


urlpatterns = [
    path('', hora_extra_list, name='hora-extra-list'),
    path('create/', hora_extra_create, name='hora-extra-create'),
    path('edit/<int:id>', hora_extra_edit, name='hora-extra-edit'),
    path('edit-funcionario/<int:id>', hora_extra_edit_funcionario, name='hora-extra-edit-funcionario'),
    path('used-time-bank/<int:id>', hora_extra_utilizada, name='hora-extra-used'),
    path('delete/<int:id>', hora_extra_delete, name='hora-extra-delete'),
]