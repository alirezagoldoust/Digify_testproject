from django.urls import path
from .views import OrderList, OrderListTest, order_list_view

urlpatterns = [
    path('orders/', OrderList.as_view(), name='list'),
    path('test/', OrderListTest.as_view(), name='test'),
    # path('test/', order_list_view, name='test'),
]
