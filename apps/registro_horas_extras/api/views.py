from rest_framework import viewsets
from apps.registro_horas_extras.api.serializers import RegistroHoraExtraSerializer
from apps.registro_horas_extras.models import RegistroHoraExtra
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class RegistroHoraExtraViewSet(viewsets.ModelViewSet):
    queryset = RegistroHoraExtra.objects.all()
    serializer_class = RegistroHoraExtraSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)