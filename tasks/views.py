import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, ListView

from .forms import TaskCreateForm
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


class TaskCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks')
    missed_rights_message = _('You do not have permission to modify task.')
    need_loging_message = _('You are not authorized! Please sign in.')
    success_message = _('Task successfully created')
    form_class = TaskCreateForm

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, self.missed_rights_message)
            return redirect('tasks')
        messages.error(self.request, self.need_loging_message)
        return redirect('login')

    def form_valid(self, form):
        form.instance.creator = User.objects.get(id=self.request.user.id)
        return super().form_valid(form)
