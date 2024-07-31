from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.db.models import F
from .models import Order, Store

def get_products(request):
    orders = list(Order.objects.select_related('store').annotate(store_name=F('store__name')).values('id', 'cost', 'store_name'))
    print(orders)
    return JsonResponse(orders, safe=False)

