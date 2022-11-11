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

class Assetinfo(models.Model):
    tag_no = models.IntegerField()
    ownerID = models.CharField(max_length=20,default='')
    itemId = models.CharField(max_length=20)
    entry_date = models.DateField(default=datetime.now)
    statusID = models.CharField(max_length=20)


class Department(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20,default='')
    
class Item(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20,default='')
    categoryId = models.CharField(max_length=20)
    
class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20,default='')
    
