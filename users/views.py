from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import DeleteView, ListView, UpdateView, CreateView

from .forms import UserCreateForm


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
    # _('You do not have permission to modify another user.')
    success_message = _('Your account has been updated!')
    fields = ['first_name', 'last_name', 'username']

    def test_func(self):
        user = self.get_object()
        if self.request.user.id == user.id:
            return True
        return False


class UserDeleteView(SuccessMessageMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('tasks-home')
    success_message = _('User deleted successfully')

    def test_func(self):
        user = self.get_object()
        if self.request.user.id == user.id:
            return True
        return False
