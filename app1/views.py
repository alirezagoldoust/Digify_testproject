from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListAPIView
from django.http import JsonResponse
from django.db.models import F
from django.db import connection, reset_queries
from .models import Order, Store
from .serializer import OrderSerializer, StoreSerializer

# def get_orders(request):
    # orders = list(Order.objects.select_related('store').annotate(store_name=F('store__name')).values('id', 'cost', 'store_name'))
    # print(orders)
    # return JsonResponse(orders, safe=False)

class OrderList(ListAPIView):
    # reset_queries()
    queryset = Order.objects.select_related('store').annotate(store_name=F('store__name'))
    serializer_class = OrderSerializer

