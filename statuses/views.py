from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from .models import Status
from django.views.generic import CreateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from .forms import StatusCreateForm  # noqa: WPS300. Ignore local folder import


class StatusListView(ListView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'


class StatusCreateView(SuccessMessageMixin, CreateView):
    model = Status
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses')
    form_class = StatusCreateForm
    success_message = _('Status successfully created')
