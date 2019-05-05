import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from home.models import Customer, Price, Order


def home_page(request):
    return render(request, 'base.html')


def get_customer(request):
    if request.is_ajax():
        if request.POST.get('query'):
            query = request.POST.get('query')
            all_cust = Customer.objects.filter(Q(name__contains=query) | Q(mobile__contains=query))
            customer_dict = {}
            for each in all_cust:
                customer_dict[each.id] = {
                    'name': each.name,
                    'mobile': each.mobile
                }
            return HttpResponse(json.dumps(customer_dict))
        else:
            return HttpResponse('Error:Null query')
    else:
        return HttpResponse('Error:Not ajax')


def get_reports(request):
    return render(request, 'reports.html')


def customer_registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')

        cust_obj = Customer.objects.create(name=name, email=email, mobile=mobile, address=address)

        return HttpResponse('Successfully registered')
    else:
        return HttpResponse('Not Post')


def new_order(request, customer_id):
    c_id = int(customer_id)
    customer_obj = Customer.objects.filter(id=c_id)

    if len(customer_obj) == 1:
        customer_obj = customer_obj[0]

        if request.method == 'POST':
            kg = float(request.POST.get('kg'))
            if kg < 0:
                price_json = {}
                all_price = Price.objects.all().order_by('kg')
                for each_price in all_price:
                    price_json[str(each_price.kg)] = each_price.cost
                return render(request, 'new_order.html', {
                    'customer_obj': customer_obj,
                    'price_json': json.dumps(price_json),
                    'message_type': 'error',
                    'message': 'Kg should be greater than 0'
                })
            current_price = Price.objects.order_by('-kg').filter(kg__lte=kg)[:1][0]
            print(current_price.cost)
            order_obj = Order.objects.create(customer=customer_obj, kg=kg, received_date=datetime.date.today())
            return HttpResponse('Order saved with id' + str(order_obj.pk))
        else:
            all_price = Price.objects.all().order_by('kg')
            price_json = {}
            for each_price in all_price:
                price_json[str(each_price.kg)] = each_price.cost
            return render(request, 'new_order.html', {
                'customer_obj': customer_obj,
                'price_json': json.dumps(price_json),
            })
    else:
        return HttpResponse('No objects found with that id')
