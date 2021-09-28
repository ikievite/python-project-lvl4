from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from .models import Status
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from .forms import StatusCreateForm  # noqa: WPS300. Ignore local folder import
from django.contrib.auth.mixins import LoginRequiredMixin


class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    need_loging_message = _('You are not authorized! Please sign in.')

    def handle_no_permission(self):
        messages.error(self.request, self.need_loging_message)
        return redirect('login')


class StatusCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Status
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses')
    missed_rights_message = _('You do not have permission to modify status.')
    need_loging_message = _('You are not authorized! Please sign in.')
    success_message = _('Status successfully created')
    form_class = StatusCreateForm

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, self.missed_rights_message)
            return redirect('statuses')
        messages.error(self.request, self.need_loging_message)
        return redirect('login')


class StatusUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Status
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses')
    missed_rights_message = _('You do not have permission to modify status.')
    need_loging_message = _('You are not authorized! Please sign in.')
    success_message = _('Status changed successfully ')
    form_class = StatusCreateForm

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, self.missed_rights_message)
            return redirect('statuses')
        messages.error(self.request, self.need_loging_message)
        return redirect('login')


class StatusDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = _('Status deleted successfully')
    missed_rights_message = _('You do not have permission to modify status.')
    need_loging_message = _('You are not authorized! Please sign in.')

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, self.missed_rights_message)
            return redirect('statuses')
        messages.error(self.request, self.need_loging_message)
        return redirect('login')
