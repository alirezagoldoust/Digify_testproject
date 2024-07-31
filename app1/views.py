from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListAPIView
from django.http import JsonResponse
from django.db.models import F
from django.db import connection, reset_queries
from .models import Order, Store
from .serializer import OrderSerializer, StoreSerializer

# def order_list_view(request):
    # orders = list(Order.objects.select_related('store').annotate(store_name=F('store__name')).orders.values('id', 'cost', 'store_name'))
    # return JsonResponse(orders, safe=False)

class OrderList(ListAPIView):
    queryset = Order.objects.select_related('store').annotate(store_name=F('store__name'))
    serializer_class = OrderSerializer

