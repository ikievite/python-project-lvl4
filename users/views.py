from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import DeleteView, UpdateView

from .forms import UserCreateForm


def users(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'users/users.html', {'users': users})


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
