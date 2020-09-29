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


class CartItemModel(models.Model):
    id=models.AutoField(primary_key=True)
    customer=models.ForeignKey(CustomerRegistrationModel,on_delete=models.CASCADE,default=False)
    food=models.ForeignKey(FoodItemsModel,on_delete=models.CASCADE,default=False)
    quantity=models.IntegerField(default=False)
    status=models.CharField(max_length=50,default="Active")


class OrderModel(models.Model):
    id=models.AutoField(primary_key=True)
    c_id=models.ForeignKey(CustomerRegistrationModel,on_delete=models.CASCADE,default=False)
    total=models.FloatField()
    date=models.DateField(auto_now_add=True)
    address=models.TextField()
