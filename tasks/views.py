import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _
from django.views.generic import ListView

from .models import Task

logger = logging.getLogger(__name__)


def index(request):
    logger.error('log msg')
    return render(request, 'tasks/index.html', context={
        'greeting': _('Hello, World'),
    })


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks'
    need_loging_message = _('You are not authorized! Please sign in.')

    def handle_no_permission(self):
        messages.error(self.request, self.need_loging_message)
        return redirect('login')
