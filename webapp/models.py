from django.db import models


class Repo(models.Model):
    name = models.CharField(max_length=150)
    creation_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()

    def __str__(self):
        return self.name
