from rest_framework import serializers
from apps.funcionarios.models import Funcionario
from apps.registro_horas_extras.api.serializers import RegistroHoraExtraSerializer


class FuncionarioSerializer(serializers.ModelSerializer):
    registrohoraextra_set = RegistroHoraExtraSerializer(many=True)
    class Meta:
        model = Funcionario
        fields = ('nome', 'departamentos', 'empresa', 'user', 'imagem', 'total_horas_extras', 'registrohoraextra_set')