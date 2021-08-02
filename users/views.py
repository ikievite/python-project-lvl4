from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView
from django.contrib.auth.models import User
from .forms import UserCreateForm, UserUpdateForm


def users(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'users/users.html', {'users': users})


def create(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _(f'Your account has been created! You are now able to log in'))
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'users/create.html', {'form': form})


@login_required
def update(request, username_id):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, _('Your account has been updated!'))
            return redirect('update-user', username_id=request.user.id)
    else:
        if username_id == request.user.id:
            form = UserUpdateForm(instance=request.user)
        else:
            messages.error(request, _('You do not have permission to modify another user.'))
            return redirect('users')
    context = {
        'form': form,
    }

    return render(request, 'users/update.html', context)


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = '/'

    def test_func(self):
        user = self.get_object()
        if self.request.user.id == user.id:
            return True
        return False
