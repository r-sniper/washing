from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from home.models import Customer


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


def new_order(request,customer_id):
    if request.method == 'POST':
        kg = request.POST.get('kg')
    else:
        c_id = int(customer_id)
        customer_obj = Customer.objects.filter(id=c_id)
        if len(customer_obj) == 1:
            customer_obj = customer_obj[0]
        else:
            return HttpResponse('No objects found with that id')

# def get_cost(re)
