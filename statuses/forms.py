from django import forms
from .models import Status
from django.forms import ModelForm


class StatusCreateForm(ModelForm):
    name = forms.CharField()

    class Meta:
        model = Status
        fields = ['name']
