from django.contrib import admin

# Register your models here.
from home.models import Customer, Price, Category, Order, OrderDetail, Expense, Money

admin.site.register(Customer)
admin.site.register(Price)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Expense)
admin.site.register(Money)
