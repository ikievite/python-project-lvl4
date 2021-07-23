from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


def users(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'users/users.html', {'users': users})


def create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/create.html', {'form': form})
