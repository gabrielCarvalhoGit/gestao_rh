from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Departamento
from .forms import DepartamentoForm


@login_required(login_url='accounts/login')
def departamento_list(request):
    empresa_logada = request.user.funcionario.empresa
    departamento_list = Departamento.objects.all().order_by('nome').filter(empresa=empresa_logada)

    return render(request, 'departamentos/list.html', {'departamentos': departamento_list})

@login_required(login_url='accounts/login')
def departamento_create(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)

        if form.is_valid():
            departamento = form.save(commit=False)
            departamento.empresa = request.user.funcionario.empresa

            departamento.save()
            return redirect('departamento-list')
        
    form = DepartamentoForm()
    return render(request, 'departamentos/create_departamento.html', {'form': form})

@login_required(login_url='accounts/login')
def departamento_edit(request, id):
    departamento = get_object_or_404(Departamento, pk=id)
    form = DepartamentoForm(instance=departamento)

    if request.method == 'POST':
        form = DepartamentoForm(request.POST, instance=departamento)

        if form.is_valid():
            departamento.save()
            return redirect('departamento-list')
        else:
            return render(request, 'departamentos/edit_departamento.html', {'form': form, 'departamento': departamento})
    else:
        return render(request, 'departamentos/edit_departamento.html', {'form': form, 'departamento': departamento})

@login_required(login_url='accounts/login')
def departamento_delete(request, id):
    departamento = get_object_or_404(Departamento, pk=id)
    departamento.delete()

    messages.info(request, 'Departamento excluido com sucesso')
    return redirect('departamento-list')