from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import EmpresaForm
from .models import Empresa


@login_required(login_url='accounts/login')
def add_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)

        if form.is_valid():
            empresa = form.save(commit=False)
            empresa.save()

            funcionario = request.user.funcionario
            funcionario.empresa = empresa
            funcionario.save()
            
            return redirect('/')
        
    form = EmpresaForm()
    return render(request, 'empresas/add_empresa.html', {'form': form})

@login_required(login_url='accounts/login')
def edit_empresa(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    form = EmpresaForm(instance=empresa)

    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'empresas/edit_empresa.html', {'form': form, 'empresa': empresa})
    else:
        return render(request, 'empresas/edit_empresa.html', {'form': form, 'empresa': empresa})