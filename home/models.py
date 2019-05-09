from django.contrib.auth.models import User
from django.db import models

from home.email_sender import send_email


# Create your models here.


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
        subject = ''
        msg = ''
        if self.status == 1:
            subject = 'Order Received'
            msg = '<b>Order Details:</b><br>' \
                  'Total Weight: ' + str(self.kg) + '<br>Price: ' + str(self.price)
        elif self.status == 2:
            subject = 'Order Details'
            msg = '<b>Order Details:</b><br>' \
                  'Order No: ' + str(self.pk) + '<br>Total Weight: ' + str(self.kg) + ' Kg<br>Price: ' + str(self.price) \
                  + '<br><b>Clothes Type</b><br>'
            tmp = ''
            for each in self.orderdetail_set.all():
                if each.count > 0:
                    tmp += each.category.name + ': ' + str(each.count) + '<br>'
            msg += tmp
        elif self.status == 3:
            subject = 'Order Pick-up Reminder'
            msg = 'Order Details<br>' \
                  'Order No: ' + str(self.pk) + '<br>Total Weight: ' + str(self.kg) + ' Kg<br>Price: ' + str(
                self.price) + '<br>Order No: ' + str(self.pk) \
                  + '<br><br>Your order has been successfully washed. Kindly collect your clothes from Wool World.<br>' \
                  + '<br>Hope to be at your service again.'
        elif self.status == 4:
            subject = 'Order Delivered'
            msg = 'Order Details<br>' \
                  'Order No: ' + str(self.pk) + '<br>Total Weight: ' + str(self.kg) + ' Kg<br>Price: ' + str(self.price) \
                  + '<br>Your order has been successfully delivered on <br>' + (
                      self.delivery_date.strftime('%d %m %y, %I %M %p')) \
                  + '<br><br>Hope to be at your service again.'

        send_email(self.customer.email, subject, msg)
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
