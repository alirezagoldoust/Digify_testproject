from django.shortcuts import render, HttpResponse
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.db.models import F, Count, Avg
from django.db import connection, reset_queries
from .models import Order, Store
from .serializer import OrderSerializer, StoreSerializer

def order_list_view(request):
    orders = Order.objects.select_related('store').annotate(store_name=F('store__name'))
    orders = list(orders.values('id', 'cost'))
    return JsonResponse(orders, safe=False)

class OrderList(ListAPIView):
    queryset = Order.objects.select_related('store').annotate(store_name=F('store__name'), store_avg_price=Avg('store__orders__cost'))
    serializer_class = OrderSerializer

class OrderListTest(APIView):
    serializer_class = OrderSerializer
    def get(self, request):
        reset_queries()
        # data = Order.objects.select_related('store').all()
        data = Order.objects.all()
        for i in data:
            if i.store.domain.endswith('.com'):
                pass
        serializer = OrderSerializer(data, many=True)
        return Response(serializer.data)




