from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime

# Create your models here.

class Product(models.Model):
    product_id = models.CharField(max_length=10)
    
    def __str__(self):
        return self.product_id


class Location(models.Model):
    location_id = models.CharField(max_length=10)

    def __str__(self):
        return self.location_id


class ProductMovement(models.Model):
    movement_id = models.CharField(max_length=20,primary_key=True)
    timestamp = models.DateTimeField(default=datetime.now)
    from_location = models.ForeignKey(Location,related_name='from_location_id', on_delete=models.CASCADE,blank=True,null=True, default=None)
    to_location = models.ForeignKey(Location,related_name='to_location_id', on_delete=models.CASCADE,blank=True,null=True, default=None)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE, default=None)

    qty = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.movement_id




