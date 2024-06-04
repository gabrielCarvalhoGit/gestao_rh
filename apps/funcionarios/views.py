from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Funcionario
from .forms import FuncionarioForm


@login_required(login_url='accounts/login')
def funcionario_list(request):
    empresa_logada = request.user.funcionario.empresa
    funcionario_list = Funcionario.objects.all().order_by('nome').filter(empresa=empresa_logada)

    return render(request, 'funcionarios/list.html', {'funcionarios': funcionario_list})

@login_required(login_url='accounts/login')
def funcionario_create(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)

        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.empresa = request.user.funcionario.empresa
            funcionario.user = User.objects.create(username=f'{funcionario.nome.split(' ')[0]}')

            funcionario.save()
            return redirect('funcionario-list')
        
    form = FuncionarioForm()
    return render(request, 'funcionarios/create_funcionario.html', {'form': form})

@login_required(login_url='accounts/login')
def funcionario_edit(request, id):
    funcionario = get_object_or_404(Funcionario, pk=id)
    form = FuncionarioForm(instance=funcionario)

    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)

        if form.is_valid():
            funcionario.save()
            return redirect('funcionario-list')
        else:
            return render(request, 'funcionarios/edit_funcionario.html', {'form': form, 'funcionario': funcionario})
    else:
        return render(request, 'funcionarios/edit_funcionario.html', {'form': form, 'funcionario': funcionario})

@login_required(login_url='accounts/login')
def funcionario_delete(request, id):
    funcionario = get_object_or_404(Funcionario, pk=id)
    funcionario.delete()

    messages.info(request, 'Funcionario excluido comm sucesso')
    return redirect('funcionario-list')