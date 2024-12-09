from django.db import models

class Employee(models.Model):

    POSITIONS = [
        ("E","Employee"),
        ("A","Administrator")
    ]

    id = models.IntegerField(primary_key=True)
    password = models.CharField (max_length=100)
    login = models.CharField (max_length=100)
    firstname = models.CharField (max_length=20)
    lastname = models.CharField(max_length=100)
    phone = models.CharField (max_length=12)
    position = models.CharField (max_length=2, choices = POSITIONS)

class Product(models.Model):
    CATEGORIES = [
        ("TAB","Tableware"),
        ("CAT", "Coffee and Tea"),
        ("DEC", "Decorations")
    ]

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    photo = models.URLField()
    introduction_date = models.DateField()
    producer = models.CharField (max_length=100)
    stock = models.IntegerField()
    SKU = models.IntegerField()
    category = models.CharField (max_length=3, choices = CATEGORIES)


class Discount(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField (max_length=100)
    description = models.TextField()
    percentage = models.FloatField (default=0.0)
    start_date = models.DateField
    products = models.ManyToManyField(Product)
    end_date = models.DateField

class Client(models.Model):
    id = models.IntegerField(primary_key=True)
    email = models.CharField (max_length=100)
    name = models.CharField (max_length=100)
    password = models.CharField (max_length=100)
    login = models.CharField (max_length=100)
    firstname = models.CharField (max_length=20)
    lastname = models.CharField(max_length=100)
    phone = models.CharField (max_length=12)
    wishlist = models.ManyToManyField(Product)

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
    date = models.DateField()
    amount = models.FloatField()
    status = models.CharField (max_length=3, choices = STATUS)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    destination_country = models.CharField (max_length=12, choices=COUNTRY)
    destination_region = models.CharField (max_length=20)
    destination_city = models.CharField (max_length=20)
    destination_postcode = models.CharField (max_length=10)
    payment_method = models.CharField (max_length=2, choices = METHOD)

class Cart(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.IntegerField()

