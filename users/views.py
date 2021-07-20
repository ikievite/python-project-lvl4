from django.shortcuts import render
from django.contrib.auth import get_user_model


def users(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'users/users.html', {'users': users})
