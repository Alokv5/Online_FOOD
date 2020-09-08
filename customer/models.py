from django.db import models

from vendor.models import FoodItemsModel
from foodAdmin.models import CityModel

class CustomerRegistrationModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    contact=models.IntegerField(unique=True)
    address=models.TextField()
    city=models.ForeignKey(CityModel,on_delete=models.CASCADE)
    password=models.CharField(max_length=30)
    otp=models.IntegerField()



class OrderModel(models.Model):
    id=models.AutoField(primary_key=True)
    items=models.ManyToManyField(FoodItemsModel)
    quantity=models.IntegerField()
    total=models.FloatField()
    status=models.CharField(max_length=20)
    date=models.DateField(auto_now_add=True)
    address=models.TextField()