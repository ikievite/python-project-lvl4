from django.contrib.auth.models import User
from django.db import models

from statuses.models import Status


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='task_author')
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='task_executor',
        null=True,
        blank=True,
    )
    status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)

    def __str__(self):
        return self.name
