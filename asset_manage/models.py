from datetime import datetime
from email.policy import default
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User



class Asset(models.Model):
    title = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    description = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
         return self.title

class Assetinfo(models.Model):
    tag_no = models.IntegerField()
    ownerID = models.CharField(max_length=20,default='')
    item_id = models.CharField(max_length=20,default='')
    entry_date = models.DateField(default=datetime.now)
    statusID = models.CharField(max_length=20)
    def __str__(self):
        return self.item_id

class Department(models.Model):
    department_id = models.IntegerField(primary_key=True)
    department_name = models.CharField(max_length=20,default='')
    
class Item(models.Model):
    item_id = models.ForeignKey(Assetinfo, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=20,default='')
    categoryId = models.CharField(max_length=20)
    
class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=20,default='')

class Employeeinfo(models.Model):
    empolyeeID = models.IntegerField()
    employeeName = models.CharField(max_length=20,default='')
    departmentId = models.IntegerField()
    contact = models.IntegerField()
    email = models.CharField(max_length=20)

class Assetstatus(models.Model):
    statusid = models.IntegerField(primary_key=True)
    statusname = models.CharField(max_length=20,default='')    
