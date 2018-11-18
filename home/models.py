from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Customer(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    kg = models.DecimalField()
    received_date = models.DateField()
    delivery_date = models.DateField(null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    count = models.IntegerField(default=0)

class Price(models.Model):
    kg = models.DecimalField()
    cost = models.PositiveIntegerField()