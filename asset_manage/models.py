from datetime import datetime
from email.policy import default
from django.db import models
from django.utils.timezone import now


class Asset(models.Model):
    title = models.CharField(max_length=20)
    owner = models.CharField(max_length=20,default='')
    date = models.DateField(default=datetime.now)
    description = models.CharField(max_length=100)
    price = models.IntegerField()

