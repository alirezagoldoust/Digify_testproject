from .models import Order, Store
from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    store_name = serializers.CharField(required=False)
    store_avg_price = serializers.IntegerField(required=False)
    class Meta:
        model = Order
        exclude = ['store']

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'