from django.shortcuts import render

from .models import Status
from django.views.generic import CreateView, DeleteView, ListView


class StatusListView(ListView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
