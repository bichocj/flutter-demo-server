from rest_framework import exceptions, serializers
from . import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
            model = models.Product
            fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    #product = ProductSerializer()

    class Meta:
            model = models.OrderItem
            fields = '__all__'
            #fields = ('product','quantity','total')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer()
    class Meta:
            model = models.Order
            fields = ('client', 'items')
