from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.utils.translation import gettext as _
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
            messages.success(request, _(f'Your account has been created! You are now able to log in'))
            return redirect('login')
    else:
        form = UserCreateForm()
    return render(request, 'users/create.html', {'form': form})
