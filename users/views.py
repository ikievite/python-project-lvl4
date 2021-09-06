from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import UserCreateForm  # noqa: WPS300. Ignore local folder import


class UserListView(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    form_class = UserCreateForm
    success_message = _('Your account has been created! You are now able to log in')


class UserUpdateView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    missed_rights_message = _('You do not have permission to modify another user.')
    need_loging_message = _('You are not authorized! Please sign in.')
    success_message = _('Your account has been updated!')
    form_class = UserCreateForm

    def test_func(self):
        user = self.get_object()
        return self.request.user.id == user.id

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, self.missed_rights_message)
            return redirect('users')
        messages.error(self.request, self.need_loging_message)
        return redirect('login')


class UserDeleteView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('tasks-home')
    success_message = _('User deleted successfully')
    missed_rights_message = _('You do not have permission to modify another user.')
    need_loging_message = _('You are not authorized! Please sign in.')

    def test_func(self):
        user = self.get_object()
        return self.request.user.id == user.id

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, self.missed_rights_message)
            return redirect('users')
        messages.error(self.request, self.need_loging_message)
        return redirect('login')
