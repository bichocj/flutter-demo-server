from django.db import models

class Client(models.Model):    
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dni = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    last_lon = models.CharField(max_length=50, default="")
    last_lat = models.CharField(max_length=50, default="")
