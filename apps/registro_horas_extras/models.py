from django.db import models
from apps.funcionarios.models import Funcionario


# Relacionamento ForeignKey => Um registro em uma tabela está associoado a vários registros de outra tabela

class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT) # models.PROTECT levantará uma excessão 'ProtectedError' caso tente excluir o usser, evitando perda de dados no banco
    horas = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.motivo