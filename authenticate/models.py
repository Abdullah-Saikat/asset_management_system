from datetime import datetime
from email.policy import default
from django.db import models
from django.utils.timezone import now


class Staff(models.Model):
	username = models.CharField(max_length=20,default='')
depertment_name=models.CharField(max_length=20,default='')
user_type= models.CharField(max_length=20,default='')