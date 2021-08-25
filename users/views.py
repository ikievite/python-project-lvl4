from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import DeleteView, ListView, UpdateView

from .forms import UserCreateForm


class UserListView(ListView):
    model = User
    template_name = 'users/users.html'
    context_object_name = 'users'


def create(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                _('Your account has been created! You are now able to log in'),
            )
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'users/create.html', {'form': form})


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    template_name = 'users/update.html'
    success_url = reverse_lazy('users')
    # _('You do not have permission to modify another user.')
    fields = ['first_name', 'last_name', 'username']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.add_message(self.request, messages.SUCCESS, _('Your account has been updated!'))
        return super().form_valid(form)

    def test_func(self):
        user = self.get_object()
        if self.request.user.id == user.id:
            return True
        return False


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = '/'
    success_message = 'User deleted successfully'

    def test_func(self):
        user = self.get_object()
        if self.request.user.id == user.id:
            return True
        return False
