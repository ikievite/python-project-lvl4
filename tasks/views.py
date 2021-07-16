import logging
from django.shortcuts import render
from django.utils.translation import gettext as _


logger = logging.getLogger(__name__)


def index(request):
    logger.error('log msg')
    return render(request, 'tasks/index.html', context={
        'greeting': _('Hello, World'),
    })
