from datetime import datetime
from django.db import models



class Employee(models.Model):

    POSITIONS = {
        "Employee",
        "Administrator"
    }

    id = models.IntegerField(primary_key=True)
    password = models.CharField (max_length=100)
    login = models.CharField (max_length=100)
    firstname = models.CharField (max_length=20)
    lastname = models.CharField(max_length=100)
    phone = models.CharField (max_length=12)
    position = models.CharField (max_length=100, choices = POSITIONS)

class Discount(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField (max_length=100)
    description = models.TextField ()
    Discount_percentage = models.FloatField (default=0.0)
    start_date = models.DateField (default=datetime.date)
    end_date = models.DateField



