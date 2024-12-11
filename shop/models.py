from django.db import models
from django.contrib.auth.models import AbstractUser

#testowanie 

class Product(models.Model):
    CATEGORIES = [
        ("TAB","Tableware"),
        ("CAT", "Coffee and Tea"),
        ("DEC", "Decorations")
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(default="")
    price = models.FloatField(default=0)
    photo = models.URLField(default="")
    introduction_date = models.DateField(default = 0)
    producer = models.CharField (max_length=100,default="")
    stock = models.IntegerField(default=0)
    SKU = models.IntegerField(default=0)
    category = models.CharField (max_length=3, choices = CATEGORIES, default="TAB")


class Discount(models.Model):
    name = models.CharField (max_length=100)
    description = models.TextField(default="")
    percentage = models.FloatField (default=0.0)
    start_date = models.DateField
    products = models.ManyToManyField(Product)
    end_date = models.DateField

class User(AbstractUser):
    email = models.CharField (max_length=100,unique=True)
    password = models.CharField (max_length=100)
    username = models.CharField (max_length=100,unique=True)
    first_name = models.CharField (max_length=20)
    last_name = models.CharField(max_length=100)
    phone = models.CharField (max_length=12)
    wishlist = models.ManyToManyField(Product)

    TYPE_OF_USER = [
        ("C","Client"),
        ("E","Employee"),
        ("A","Administrator")
    ]
    position = models.CharField (max_length=2, choices = TYPE_OF_USER)


    REQUIRED_FIELDS = []

class Order(models.Model):
    STATUS = [
        ("PEN", "Pending"),
        ("APY", "Awaiting Payment"),
        ("APC", "Awaiting Pickup"),
        ("SHI", "Shipped"),
        ("CMP", "Completed")
    ]
    COUNTRY = [
        ("PL", "Poland"),
        ("CZ", "Czech Republic"),
        ("SL", "Slovak Republic"),
        ("GE", "Germany")
    ]
    METHOD = [
        ("CR", "Card")
    ]
    id = models.IntegerField(primary_key=True)
    date = models.DateField(default="")
    amount = models.FloatField(default=0)
    status = models.CharField (max_length=3, choices = STATUS, default="PEN")
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    destination_country = models.CharField (max_length=12, choices=COUNTRY, default="PL")
    destination_region = models.CharField (max_length=20, default="")
    destination_city = models.CharField (max_length=20, default="")
    destination_postcode = models.CharField (max_length=10, default="")
    payment_method = models.CharField (max_length=2, choices = METHOD, default="CR")
    

class Cart(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.IntegerField(default=0)
    products = models.ManyToManyField(Product)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,default=1)

