from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateTimeField('date created', auto_now_add=True)

    def __str__(self):
        return self.name
