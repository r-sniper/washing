from django.contrib import admin

# Register your models here.
from home.models import Customer, Price, Category, Order, OrderDetail

admin.site.register(Customer)
admin.site.register(Price)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderDetail)
