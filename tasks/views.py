from django.shortcuts import render
from django.utils.translation import gettext as _


def index(request):
    return render(request, 'tasks/index.html', context={
        'greeting': _('Hello, World'),
    })
