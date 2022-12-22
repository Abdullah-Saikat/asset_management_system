from datetime import datetime
from email.policy import default
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class Staff(models.Model):
	username = models.CharField(max_length=20,default='')
depertment_name=models.CharField(max_length=20,default='')
user_type= models.CharField(max_length=20,default='')

user_type = (
    ("Admin", "Admin"),
    ("Staff", "Staff"),
    ("Store_man", "Store_man"),
)
class Usertype(models.Model):
	user= models.OneToOneField(User,on_delete=models.CASCADE,)
	user_type = models.CharField(
        max_length = 20,
        choices = user_type,
        default = 'Admin'
        )