from django.db import models


class Repo(models.Model):
    name = models.CharField(max_length=150)
    creation_datetime = models.DateTimeField()
    update_datetime = models.DateTimeField()

    def __str__(self):
        return self.name


class Stats(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    value = models.TextField()

    def __str__(self):
        return self.name