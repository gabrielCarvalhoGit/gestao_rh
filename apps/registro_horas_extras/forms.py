from django import forms

from .models import RegistroHoraExtra
from apps.funcionarios.models import Funcionario


class HoraExtraCreateForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(HoraExtraCreateForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.filter(
            empresa=user.funcionario.empresa)

    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionario', 'horas']

class HoraExtraEditForm(forms.ModelForm):
    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'horas']