
from time import time
from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Reservation(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    number_of_persons=models.IntegerField()
    date=models.DateField(null=True)
    time=models.TimeField(null=True)

    
    def __str__(self):
        return self.name
