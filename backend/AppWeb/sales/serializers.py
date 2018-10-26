from rest_framework import exceptions, serializers
from . import models
from clients.serializers import ClientSerializer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
            model = models.Product
            fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
            model = models.OrderItem
            fields = '__all__'
            #fields = ('product','quantity','total')

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    client = ClientSerializer()
    class Meta:
            model = models.Order
            fields = ('client', 'items',)
