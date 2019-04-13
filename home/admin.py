from django.contrib import admin

# Register your models here.
from home.models import Customer, Price

admin.site.register(Customer)
admin.site.register(Price)
