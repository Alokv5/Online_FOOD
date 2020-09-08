from django.db import models
from foodAdmin.models import CityModel,CusineModel

class VendorRegistrationModel(models.Model):
    id=models.AutoField(primary_key=True)
    stall_name=models.CharField(max_length=200)
    contact_1=models.IntegerField(unique=True)
    contact_2=models.IntegerField(unique=True)
    cuisine_type=models.ForeignKey(CusineModel,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='vendor_images/')
    address=models.TextField()
    vender_city=models.ForeignKey(CityModel,on_delete=models.CASCADE)
    password=models.CharField(max_length=20)
    OTP=models.IntegerField()
    status=models.CharField(max_length=20)


class FoodtypeModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    vender_id=models.ForeignKey(VendorRegistrationModel,on_delete=models.CASCADE)
    status = models.CharField(max_length=30,default=False)  # suspend activate

class FoodItemsModel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    food_type=models.ForeignKey(FoodtypeModel,on_delete=models.CASCADE)
    price=models.FloatField()
    photo=models.ImageField(upload_to='food_items/')

