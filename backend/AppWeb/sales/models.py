from django.db import models
from clients.models import Client

class Product(models.Model):
	product = models.CharField(max_length=50)
	price = models.DecimalField(decimal_places=2, max_digits=10)

class Order(models.Model):    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=0)
	total = models.IntegerField(default=0)
