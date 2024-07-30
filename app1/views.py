from django.shortcuts import render

# Create your views here.

# 1. Store.objects.annotate(order_num=Count("orders")).filter(order_num__gte=0).values('name', 'order_num')
# 2. Store.objects.annotate(order_num=Count("order")).values('name', 'order_num')
# 3. Store.objects.annotate(order_num=Count("order")).values('name', 'order_num')
# 4. Order.objects.aggregate(Sum("cost"))

#1.2 Order.objects.values("store__name").annotate(Count("cost"))
#2.2 Order.objects.values("store__name").annotate(Sum("cost"))