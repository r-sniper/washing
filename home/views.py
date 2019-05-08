import datetime
import json

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from home.models import Customer, Price, Order, Category, OrderDetail


def home_page(request):
    return render(request, 'home.html')


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
    cats = Category.objects.filter(is_active=True).values_list('name', flat=True)
    if len(customer_obj) == 1:
        customer_obj = customer_obj[0]

        if request.method == 'POST':
            kg = float(request.POST.get('kg'))
            price_json = {}
            all_price = Price.objects.all().order_by('kg')
            for each_price in all_price:
                price_json[str(each_price.kg)] = each_price.cost
            if kg < 0:
                return render(request, 'new_order.html', {
                    'customer_obj': customer_obj,
                    'price_json': json.dumps(price_json),
                    'message_title': 'Error',
                    'message_type': 'error',
                    'message': 'Kg should be greater than 0',
                    'category': [cats[i:i + 2] for i in range(0, len(cats), 2)]
                })
            # current_price = Price.objects.order_by('-kg').filter(kg__lte=kg)[:1][0]
            current_price = float(request.POST.get('price'))
            print(current_price)
            order_obj = Order(customer=customer_obj, kg=kg, received_date=datetime.date.today(),
                              price=current_price)

            order_obj.save()

            if request.POST.get('selected') == 'ind_kg':
                for each in request.POST:
                    if each.__contains__('cloth_'):
                        each_id = each.split('cloth_')[1]
                        cat_obj = Category.objects.get_or_create(name=request.POST.get(each), is_active=True)[0]
                        order_details = OrderDetail(order=order_obj, category=cat_obj,
                                                    count=int(request.POST.get('qty_' + each_id)))
                        order_details.save()
            return render(request, 'new_order.html', {
                'customer_obj': customer_obj,
                'price_json': json.dumps(price_json),
                'message_type': 'success',
                'message_title': 'Success',
                'message': 'Order registered for customer ' + customer_obj.name,
                'category': [cats[i:i + 2] for i in range(0, len(cats), 2)]
            })
        else:
            all_price = Price.objects.all().order_by('kg')
            price_json = {}
            for each_price in all_price:
                price_json[str(each_price.kg)] = each_price.cost

            return render(request, 'new_order.html', {
                'customer_obj': customer_obj,
                'price_json': json.dumps(price_json),
                'category': [cats[i:i + 2] for i in range(0, len(cats), 2)]
            })
    else:
        return HttpResponse('No objects found with that id')
