from django.db import models
from django.contrib.auth.models import User

from apps.empresas.models import Empresa
from apps.departamentos.models import Departamento


# Relacionamento OneToOne => Um registro em uma tabela está associado a exatamente um registro em outra tabela
# Relacionamento ManyToMany =: Vários registros de uma tabela podem estar associados a vários registros de outra tabela
# Relacionamento ForeignKey => Um registro em uma tabela está associoado a vários registros de outra tabela

# null=True permite que o campo seja nulo no banco de dados
# blank=True permite que o campo não seja preenchido no formulário de criação/modificação,

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT) # models.PROTECT levantará uma excessão 'ProtectedError' caso tente excluir o usser, evitando perda de dados no banco
    departamento = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nome