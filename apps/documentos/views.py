from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView

from .models import Documento
from .forms import DocumentoForm
from apps.funcionarios.models import Funcionario


class DocumentoCreate(CreateView):
    model = Documento
    form_class = DocumentoForm
    template_name = 'documentos/documento_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['funcionario'] = get_object_or_404(Funcionario, pk=self.kwargs['funcionario_id'])
        return context

    def form_valid(self, form):
        form.instance.pertence = get_object_or_404(Funcionario, pk=self.kwargs['funcionario_id'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('funcionario-list')