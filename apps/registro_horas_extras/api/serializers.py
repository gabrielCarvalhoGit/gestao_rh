from rest_framework import serializers
from apps.registro_horas_extras.models import RegistroHoraExtra


class RegistroHoraExtraSerializer(serializers.ModelSerializer):
    class Meta: 
        model = RegistroHoraExtra
        fields = ('motivo', 'funcionario', 'horas', 'hora_utilizada')