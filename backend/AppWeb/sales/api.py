from rest_framework import viewsets
from . import serializers, models

class ProductViewSet(viewsets.ModelViewSet):    
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()

class OrderViewSet(viewsets.ModelViewSet):    
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()
