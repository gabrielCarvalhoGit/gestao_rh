from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import RegistroHoraExtra
from .forms import HoraExtraCreateForm, HoraExtraEditForm

@login_required(login_url='accounts/login')
def hora_extra_list(request):
    empresa_logada = request.user.funcionario.empresa
    list_horas_extras = RegistroHoraExtra.objects.all().filter(funcionario__empresa=empresa_logada)

    return render(request, 'registro_horas_extras/list.html', {'horas_extras': list_horas_extras})

@login_required(login_url='accounts/login')
def hora_extra_create(request):
    if request.method == 'POST':
        form = HoraExtraCreateForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            return redirect('hora-extra-list')
    
    form = HoraExtraCreateForm(user=request.user)
    return render(request, 'registro_horas_extras/create_hora_extra.html', {'form': form})

@login_required(login_url='accounts/login')
def hora_extra_edit(request, id):
    hora_extra = get_object_or_404(RegistroHoraExtra, pk=id)
    form = HoraExtraEditForm(instance=hora_extra)

    if request.method == 'POST':
        form = HoraExtraEditForm(request.POST, instance=hora_extra)

        if form.is_valid():
            hora_extra.save()
            return redirect('hora-extra-list')
        else:
            return render(request, 'registro_horas_extras/edit_hora_extra.html', {'form': form, 'registro': hora_extra})
    else:
        return render(request, 'registro_horas_extras/edit_hora_extra.html', {'form': form, 'registro': hora_extra})
    
@login_required(login_url='accounts/login')
def hora_extra_delete(request, id):
    hora_extra = get_object_or_404(RegistroHoraExtra, pk=id)
    hora_extra.delete()

    messages.info(request, 'Registro excluído com sucesso')
    return redirect('hora-extra-list')