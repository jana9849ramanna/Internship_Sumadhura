
from django.db import models
from django.contrib.auth.models import User

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    # Other vendor fields...

class Product(models.Model):
    name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    # Other product fields...

class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length=20)
    vehicle_type = models.CharField(max_length=50)
    delivery_challan_number = models.CharField(max_length=50)
    purchase_order_number = models.CharField(max_length=50)
    # Other vehicle fields...
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quality_check_passed = models.BooleanField(default=False)

class QualityCheck(models.Model):
    vehicle = models.OneToOneField(Vehicle, on_delete=models.CASCADE)
    passed = models.BooleanField()
    # Other quality check fields...
