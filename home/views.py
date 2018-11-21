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
