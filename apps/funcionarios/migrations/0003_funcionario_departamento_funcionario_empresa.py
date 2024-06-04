# Generated by Django 5.0.4 on 2024-05-07 19:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0002_rename_name_departamento_nome'),
        ('empresas', '0002_rename_name_empresa_nome'),
        ('funcionarios', '0002_rename_name_funcionario_nome_funcionario_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='departamento',
            field=models.ManyToManyField(to='departamentos.departamento'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
            preserve_default=False,
        ),
    ]
