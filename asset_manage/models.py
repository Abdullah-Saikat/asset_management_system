from django.db import models


class Asset(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
