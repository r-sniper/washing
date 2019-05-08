from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver


class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Customer(models.Model):
    name = models.CharField(max_length=200, null=False)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    # date_created = models.DateField()


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # user = models.ForeignKey(UserDetails, on_delete=models.CASCADE, null=True)
    kg = models.DecimalField(max_digits=6, decimal_places=2)
    received_date = models.DateTimeField()
    delivery_date = models.DateTimeField(null=True, blank=True)
    price = models.FloatField()
    status = models.CharField(default=1, max_length=1)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

        price = self.price
        date = self.delivery_date
        if date:
            money_obj = Money.objects.filter(date=date)
            if len(money_obj) > 0:
                money_obj = money_obj[0]
                money_obj.total_income += price
            else:
                Money.objects.create(date=date, total_income=price)


# 1: only kg
# 2: clothwise
# 3: completed washing
# 4: delivered

class Category(models.Model):
    name = models.CharField(max_length=100)
    # to_show = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.category.name + ' ' + str(self.count)


class Price(models.Model):
    kg = models.DecimalField(max_digits=6, decimal_places=2)
    cost = models.FloatField()


class Expense(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField()
    cost = models.FloatField()

    def save(self, *args, **kwargs):
        super(Expense, self).save(*args, **kwargs)
        # print('called')
        cost = self.cost
        date = self.date
        money_obj = Money.objects.filter(date=date)
        if len(money_obj) > 0:
            money_obj = money_obj[0]
            money_obj.total_expenditure += cost
        else:
            Money.objects.create(date=date, total_expenditure=cost)


class Money(models.Model):
    date = models.DateField(unique=True)
    total_income = models.FloatField(default=0)
    total_expenditure = models.FloatField(default=0)
